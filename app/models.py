from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
import json
from . import db, login_manager
import os



class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    # 確認密碼是否正確
    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User %r>' % self.username


class Article(db.Model):
    __tablename__ = 'article'
    pid = db.Column(db.BigInteger, primary_key=True)
    title = db.Column(db.String(64))
    author = db.Column(db.String(11))
    content = db.Column(db.String(128))
    scontent = db.Column(db.String(64))
    date = db.Column(db.Date,index=True)
    article_type = db.Column(db.String(11), index=True)
    tag = db.Column(db.String(11))
    view = db.Column(db.Integer)
    url_from = db.Column(db.String(11), unique=True)
    pic_count = db.Column(db.Integer)
    sort = db.Column(db.Integer)

    def make_json_auto(self):
        data = self.query.all()
        cols = ['pid','scontent','date','article_type','title']
        result = [{col: getattr(d, col) for col in cols} for d in data]
        with open(os.path.expanduser("~/Desktop/flask/bigdata/app/static/json/news1.json"), 'w+') as file:
            json.dump(result,file)
            file.close()

    def __repr__(self):
        return '<Article %r>' % self.pid


class Tag(db.Model):
    __tablename__ = 'tag'
    id = db.Column(db.Integer, primary_key=True)


    def __repr__(self):
        return '<Tag %r>' % self.name


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))