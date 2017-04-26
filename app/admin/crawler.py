import requests,re,json
from bs4 import BeautifulSoup


def get_html(url):
    s = requests.session()
    headers = {
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
        ,"Accept-Encoding":"gzip, deflate, sdch"
        ,"Accept-Language":"zh-CN,zh;q=0.8,en;q=0.6,la;q=0.4"
        ,"Cache-Control":"no-cache"
        ,"Connection":"keep-alive"
        ,"Cookie":"Hm_lvt_46db1c7ab0c594c8219d3a3d68e66ff8=1488466544; Hm_lpvt_46db1c7ab0c594c8219d3a3d68e66ff8=1490158290"
        ,"Host":"www.36dsj.com"
        ,"Pragma":"no-cache"
        ,"Referer":"http://www.36dsj.com/?s=spark"
        ,"Upgrade-Insecure-Requests":"1"
        ,"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
    }

   
    #發送數據請求
    r = s.get(url,headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    #soup.article.prettify()
    return soup



#下載圖片
from io import StringIO,BytesIO
from PIL import Image
def download_img(pid,url,path,pcount,article_type):

    image_name = pid+'_'+str(pcount)+'.jpg'
    r = requests.get(url)
    s = BytesIO(r.content)
    i = Image.open(s)
    i.save(path+'/'+article_type+'/'+image_name)



# 簡轉繁
from .langconv import *
# 转换简体到繁体
def chs_to_cht(line):
    line = Converter('zh-hant').convert(line)
    line.encode('utf-8')
    return line



def get_info(pid,url,path,article_type):

    soup = get_html(url)

    # maek title
    title = chs_to_cht(str(soup.title.string).replace('36','BIN '))

    # make content
    pcount = 0
    for a_tag in soup.article.find_all('img'):
        pcount = pcount + 1
        download_img(pid,a_tag['src'],path,pcount,article_type)
        a_tag['src'] = "../static/pic/"+article_type+"/"+pid+"_"+str(pcount)+".jpg"
        a_tag['class'] = "36img"
        del a_tag['width'],a_tag['height'],a_tag['sizes'],a_tag['srcset']
    content = chs_to_cht(str(soup.article))
    content = content.replace('\r\n','<br>').replace('\u2028','').replace('\\\\','\\').replace('\\','').replace('\n','')

    # make scontent
    soup = BeautifulSoup(content, 'html.parser')
    for a_tag in soup.article.find_all('p'):
        if a_tag.string is not None and len(a_tag.string)>20 :
            scontent = a_tag.string
            break

    result = [title,content,scontent,pcount]
    return result
