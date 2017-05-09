from ..models import User,Article
import os,json

def make_json():
	data = Article.query.order_by(Article.pid.desc()).all()
	cols = ['pid','scontent','date','article_type','title']
	result = [{col: getattr(d, col) for col in cols} for d in data]
	path = os.getcwd()
	#with open("/app/app/static/json/news1.json", 'w+') as file:
	with open(os.path.expanduser(path+"/app/static/json/news1.json"), 'w+') as file:
		json.dump(result,file)
		file.close()