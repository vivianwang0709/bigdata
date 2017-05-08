from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SelectField,\
 SubmitField,TextAreaField,FileField
from wtforms.validators import Required
from wtforms import ValidationError
from flask_pagedown.fields import PageDownField


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


class EditForm(FlaskForm):
    title = PageDownField("Article Title", validators=[Required()])
    article_type = SelectField('Article Type',choices=[('1','code'),('2','analysis'),('3','news'),('4','learn')])
    scontent = PageDownField("Article Scontent", validators=[Required()])
    content = PageDownField("Article Content", validators=[Required()])
    submit = SubmitField("Save it")


class mkUploadForm(FlaskForm):
    title = StringField("Article Title", validators=[Required()])
    author = StringField('Author', validators=[Required()])
    article_type = SelectField('Article Type',choices=[('1','code'),('2','analysis'),('3','news'),('4','learn')])
    file = FileField('File Upload',render_kw={'multiple':True})
    scontent = TextAreaField("Article Scontent", validators=[Required()])    
    mkcontent = PageDownField("MarkDown Content", validators=[Required()])
    submit = SubmitField('Submit')




