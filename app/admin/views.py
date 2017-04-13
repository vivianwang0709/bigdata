from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user, logout_user, login_required, \
    current_user

# 導入init的db
from .. import db
from ..models import User,Article
from . import admin
from .forms import LoginForm,UploadForm
from .crawler import *

import os
import datetime


# @admin.route('/success')
# def success():
#     return render_template('back/success.html')


@admin.route('/upload', methods=['GET', 'POST'])
@login_required
def upload():

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
        cdata = get_info(str(pid) , url, path+"/app/static/pic/", article_type)
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

    return render_template('back/upload.html', form=form)



@admin.route('/login', methods=['GET', 'POST'])
def login():

    form = LoginForm()
    
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        # 登陸資訊正確，進入後台系統
        if user is not None and user.verify_password(form.password.data):
            login_user(user,form.remember_me.data)
            return redirect(url_for('main.home'))

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
