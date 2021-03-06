from flask import render_template,request
from . import main
from .. import db
from ..models import User,Article


@main.route('/')
def home():
    num = Article.query.count()
    article = Article.query.order_by(Article.pid.desc())[:5]
    return render_template('main/home.html',article=article,num=num)


#路由：關於我
@main.route('/aboutus')
def about():
    return render_template('main/aboutus.html')


#文章分類頁：article/news
#文章內容頁：article/news?pageid=1
@main.route('/post/<string:name>')
def post(name):
    tag = {'code':"大數據技術框架",'news':"大數據產業動向",'analysis':"大數據分析",'learn':"大數據教程"}
    pageid = request.args.get('pageid')

    if pageid is not None:
        posts = Article().query.filter_by(pid=pageid).all()
        return render_template('main/article.html',posts=posts)
        #return render_template('article/'+name+'_'+str(pageid)+'.html')
    if name in tag:
        num = Article.query.filter_by(article_type=name).count()
        article = Article.query.filter_by(article_type=name).order_by(Article.pid.desc())[:5]
        return render_template('main/post.html',article=article,title=tag[name],type=name,num=num)


@main.route('/get/<int:num>', methods=['GET', 'POST'])
def getPost(num):
    num = int(num)
    type = request.args.get('type')
    if type is not None:
        article = Article.query.filter_by(article_type=type).order_by(Article.pid.desc())[(num-1)*5:num*5]
    else:
        article = Article.query.order_by(Article.pid.desc())[(num-1)*5:num*5]
    return render_template('main/get.html',article=article)


@main.route('/test')
def test():
    return render_template('main/e6.html')



