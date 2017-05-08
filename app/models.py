from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
import json,os
from . import db, login_manager
from markdown import markdown
import bleach


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
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
    title = db.Column(db.String(1000))
    author = db.Column(db.String(128))
    content = db.Column(db.Text())
    mkcontent = db.Column(db.Text())
    scontent = db.Column(db.Text())
    date = db.Column(db.String(128),index=True)
    article_type = db.Column(db.String(128), index=True)
    tag = db.Column(db.String(128))
    view = db.Column(db.Integer)
    url_from = db.Column(db.String(128), unique=True)
    pic_count = db.Column(db.Integer)
    sort = db.Column(db.Integer)

    def make_json_auto(self):
        data = self.query.all()
        cols = ['pid','scontent','date','article_type','title']
        result = [{col: getattr(d, col) for col in cols} for d in data]
        path = os.getcwd()
        with open(os.path.expanduser(path+"/app/static/json/news1.json"), 'w+') as file:
        #with open("/app/app/static/json/news1.json", 'w+') as file:
            json.dump(result,file)
            file.close()

    @staticmethod
    def convert(mkcontent):
        allowed_tags = ['a', 'abbr', 'acronym', 'b', 'blockquote', 'code',
                        'em', 'i', 'li', 'ol', 'pre', 'strong', 'ul',
                        'h1', 'h2', 'h3', 'p']
        content = bleach.linkify(bleach.clean(
            markdown(mkcontent, output_format='html'),
            tags=allowed_tags, strip=True))
        return content

    def __repr__(self):
        return '<Article %r>' % self.pid

# db.event.listen(Article.mkcontent, 'set', Article.convert)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
