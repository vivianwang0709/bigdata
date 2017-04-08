from flask import render_template,request
from . import main


@main.route('/')
def home():
    return render_template('home.html')


#路由：關於我
@main.route('/aboutus')
def about():
    return render_template('aboutus.html')


#文章分類頁：article/news
#文章內容頁：article/news?pageid=1
@main.route('/article/<string:name>')
def article(name):
    tag = {'code':"大數據技術框架",'news':"大數據產業動向",'analysis':"大數據分析",'learn':"大數據教程"}
    pageid = request.args.get('pageid')

    if pageid is not None:
        return render_template('article/'+name+'_'+str(pageid)+'.html')
    if name in tag:
        return render_template('article.html',title=tag[name])