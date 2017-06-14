from flask import render_template, redirect, request, url_for, flash, \
    make_response
from flask_login import login_user, logout_user, login_required, \
    current_user

# 導入init的db
from .. import db
from ..models import User,Article,get_engine
from . import admin
from .forms import LoginForm,UploadForm,EditForm,mkUploadForm,textUploadForm
from .crawler import *
from .autojson import *

import os,datetime,json,random
from werkzeug import secure_filename

# @admin.route('/success')
# def success():
#     return render_template('back/success.html')



#back/post?type=new&num=1
@admin.route('/post', methods=['GET', 'POST'])
@login_required
def post():

    num = request.args.get('num')
    sort = request.args.get('type')

    if num is not None:
        num = int(num)
        if sort is not None:
            article = Article.query.filter(Article.article_type==sort)[5*(num-1):5*num]
        else:
            article = Article.query.filter(Article.pid<=num*5).filter(Article.pid>=(num-1)*5)
    elif sort is not None:
        article = Article.query.filter(Article.article_type==sort)[:5]
    else:
        article = Article.query.filter(Article.pid<=5)


    if sort is not None:
        count = Article.query.filter(Article.article_type==sort).count()
    else:
        count = Article.query.count()


    return render_template('back/test.html',article=article,sort=sort,aa=int(count/5))



@admin.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit(id):
    article = Article.query.get_or_404(id)
    form = EditForm()

    if form.submit.data is True:
        if article.mode == 'mk':
            article.content = article.convert(form.mkcontent.data)
        else:
            article.content = request.form['editor']

        article.formtosave(form)
        name = form.article_type.data
        flash('The article has been updated')
        return redirect(url_for('main.post',pageid=id,name=str(name)))

    if form.review.data is True:
        if article.mode == 'mk':
            content = article.convert(form.mkcontent.data)
        else:
            content = request.form['editor']

        return render_template('back/review.html', title=form.title.data , content=content)

    form.title.data = article.title
    form.author.data = article.author
    form.article_type.data = article.article_type
    form.scontent.data = article.scontent
    form.content.data = article.content
    form.mkcontent.data = article.mkcontent

    if article.mode == 'mk':
        return render_template('back/upload_mk.html', form=form)
    else:
        return render_template('back/upload_text.html', form=form ,editor=article.content)
   

@admin.route('/jsonfile')
@login_required
def jsonfile():
    make_json()
    return render_template('back/success.html')



@admin.route('/upload')
@login_required
def upload():
    return render_template('back/upload.html')


def gen_rnd_filename():
    filename_prefix = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    return '%s%s' % (filename_prefix, str(random.randrange(1000, 10000)))


@admin.route('/ckupload/', methods=['POST', 'OPTIONS'])
@login_required
def ckupload():
    """CKEditor file upload"""
    error = ''
    url = ''
    callback = request.args.get("CKEditorFuncNum")

    if request.method == 'POST' and 'upload' in request.files:
        fileobj = request.files['upload']
        fname, fext = os.path.splitext(fileobj.filename)
        rnd_name = '%s%s' % (gen_rnd_filename(), fext)
        filepath = os.path.join(os.getcwd()+'/app/static', 'upload', rnd_name)
        fileobj.save(filepath)
        url = url_for('static', filename='%s/%s' % ('upload', rnd_name))

    else:
        error = 'post error'

    res = """<script type="text/javascript">
  window.parent.CKEDITOR.tools.callFunction(%s, '%s', '%s');
</script>""" % (callback, url, error)

    response = make_response(res)
    response.headers["Content-Type"] = "text/html"
    return response


@admin.route('/upload_text', methods=['GET', 'POST'])
@login_required
def upload_text():
    article = Article()
    form = textUploadForm()
    if form.submit.data is True:
        article.mode = 'text'
        article.content = request.form['editor']
        article.formtosave(form)
        return render_template('back/success.html',text=request.form['editor'])

    if form.review.data is True:
        return render_template('back/review.html', form=form, content=request.form['editor'])

    form.title.data = '| BIN 大數據'
    form.author.data = 'vivian'
    return render_template('back/upload_text.html', form=form)



@admin.route('/upload_mk', methods=['GET', 'POST'])
@login_required
def upload_mk():
    article = Article()
    form = mkUploadForm()
    if form.submit.data is True:
        article.mode = 'mk'
        article.formtosave(form)
        return render_template('back/success.html',text=form.review.data)

    if form.review.data is True:
        content = article.convert(form.mkcontent.data)
        return render_template('back/review.html',form=form,content=content)

    form.title.data = '| BIN 大數據'
    form.author.data = 'vivian'
    return render_template('back/upload_mk.html', form=form)



@admin.route('/upload_36', methods=['GET', 'POST'])
@login_required
def upload_36():
    article = Article()
    form = UploadForm()
    if form.validate_on_submit():
        
        path = os.getcwd()
        try:
            pid = Article.query.order_by(Article.pid.desc()).first().pid + 1
        except:
            pid = 1 

        article_type = dict(form.article_type.choices).get(form.article_type.data)
        url = form.url.data

        #[title,content,scontent,pcount]
        cdata = get_info(str(pid) , url, path+"/app/static/pic", article_type)
        
        article.mode = 'crawler'
        article.pid = pid
        article.date = datetime.datetime.now().date().strftime("%Y-%m-%d")
        article.title = cdata[0]
        article.content = cdata[1]
        article.scontent = cdata[2]
        article.pic_count = cdata[3]
        article.article_type = article_type
        article.url_from = url
        article.author = form.author.data
        db.session.add(article)
        db.session.commit()
        return render_template('back/success.html')
    
    form.author.data = 'vivian'
    return render_template('back/upload_36.html', form=form)



@admin.route('/login', methods=['GET', 'POST'])
def login():

    form = LoginForm()
    
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        # 登陸資訊正確，進入後台系統
        if user is not None and user.verify_password(form.password.data):
            login_user(user,form.remember_me.data)
            return redirect(url_for('admin.upload'))

        flash('Invalid username or password.')
    return render_template('back/login.html', form=form)


@admin.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('admin.login'))


@admin.route('/back')
def back():
	pass
