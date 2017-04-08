from flask_bootstrap import Bootstrap
from flask import Flask, request, session, redirect, url_for, render_template,jsonify

import jinja2,json

app = Flask(__name__)
Bootstrap(app)
app.config['SECRET_KEY'] = 'hard to guess string'

#UPLOAD_FOLDER = '/tmp/'
#app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/aboutus')
def about():
    return render_template('aboutus.html')

def dynamic_post(id):
    html='''{% extends "post_base.html" %}
    {% block title %}Big Data On '''+tag+'''{% endblock %}
    {% block content %}
    {% include "'''+id+'''.html" %}
    {% endblock %}'''
    print(html)
    file = codecs.open(os.path.join('templates/article',id+'.html'), "w",encoding="utf-8",errors="xmlcharrefreplace")
    file.write(html)

@app.route('/article/<string:name>')
def article(name):
    tag = {'code':"大數據技術框架",'news':"大數據產業動向",'analysis':"大數據分析",'learn':"大數據教程"}
    pageid = request.args.get('pageid')
    if pageid is not None:
        return render_template('article/'+name+'_'+str(pageid)+'.html')
    if name in tag:
        return render_template('article.html',title=tag[name])
        
import sys
import markdown
import codecs
def fileupload(name,pageid,tag):
    out_file = name.replace('.md','.html')
    
    #input_file = codecs.open(os.path.join(app.config['UPLOAD_FOLDER'],in_file), mode="r", encoding="utf-8")
    #text = input_file.read()
    path = os.path.expanduser("~/Desktop/flask/bigdata/upload/"+tag+"/"+name)
    with open(path, encoding='utf-8') as f:
        text = f.read()
    html = markdown.markdown(text)
    data='''{% extends "post_base.html" %}
    {% block title %}Big Data On '''+tag+'''{% endblock %}
    {% block content %}
    '''+html+'''
    {% endblock %}'''

    file = open (os.path.expanduser("~/Desktop/flask/bigdata/templates/article/"+tag+"_"+str(pageid)+".html"),'w')
    file.write(data)
    file.close()
    return name+' is finish covert'


#use for dict sort reverse
from collections import OrderedDict
def addjson(title,tag,content,p,pid):

    path='static/json/'+p+'.json'
    with open(path, encoding='utf-8') as data_file:
        data = json.load(data_file)
        try:
            data = OrderedDict(sorted(data.items(),reverse=True))
            pageid = int(list(data.keys())[0])+1
            if p!='post':
                pit = pageid
            else:
                pit = pid
                
        except:
            pageid = 1
            pit = 1
            data = dict(data)
    d={
        "pageid":pit,
        "title":title,
        "content":content,
        "tag":tag
    }
    with open(path, mode='w', encoding='utf-8') as f:
        data.update({str(pageid):d})
        data = OrderedDict(sorted(data.items(),reverse=True))
        json.dump(data, f)
        f.close()
        
        
    return 'json add',pit

import os 
from werkzeug import secure_filename
app.config['UPLOAD_FOLDER'] = 'static/upload'


from flask.ext.wtf import Form
from wtforms import StringField, SubmitField,FileField
from wtforms.validators import Required
class NameForm(Form):
    title = StringField('title', validators=[Required()])
    tag = StringField('tag', validators=[Required()])
    content = StringField('content', validators=[Required()])
    file = FileField('file', validators=[Required()])
    submit = SubmitField('Submit')


    
@app.route('/upload/<string:name>', methods=['GET', 'POST'])
def upload_file(name=None):
    if name!= 'adminvivian':
        return "error"
    form = NameForm()
    if request.method == 'POST':
        
        file = form.file.data
        title = form.title.data
        tag = form.tag.data
        content = form.content.data
        
        #file = request.files['file']
        filename = secure_filename(file.filename)
        #file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        
        status2,pageid = addjson(title,tag,content,tag,0)
        status3,pageid = addjson(title,tag,content,'post',pageid)
        status1 = fileupload(filename,pageid,tag)

        return 'upload success and '+ status1+status2+status3
    else:
        return render_template('upload.html',form=form)




if __name__ == '__main__':
    app.run()