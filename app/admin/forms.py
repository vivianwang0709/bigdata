from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SelectField, SubmitField
from wtforms.validators import Required
from wtforms import ValidationError


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[Required()])
    password = PasswordField('Password', validators=[Required()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Log In')


class UploadForm(FlaskForm):
    url = StringField('Url  From', validators=[Required()])
    author = StringField('Author', validators=[Required()])
    article_type = SelectField('Article Type',choices=[('1','code'),('2','analysis'),('3','news'),('4','learn')])
	#tag = SelectField('Tag')
    submit = SubmitField('Upload')