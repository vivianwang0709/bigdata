#!/usr/bin/env python

import requests,re,json
from bs4 import BeautifulSoup
import asyncio
from aiohttp import ClientSession
import time,os


# 獲取文章內容
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
    return soup


# 簡轉繁
from langconv import *
# 转换简体到繁体
def chs_to_cht(line):
    line = Converter('zh-hant').convert(line)
    line.encode('utf-8')
    return line



#下載圖片
from io import StringIO,BytesIO
from PIL import Image

async def download_img(pid,url,path,pcount,article_type):
    image_name = pid+'_'+str(pcount)+'.jpg'
    async with ClientSession() as session:
        async with session.get(url) as resp:
            i = await resp.read()
            with open(path+'/'+image_name,"wb") as f :
                f.write(i)


# database
from sqlalchemy import create_engine
engine = create_engine('postgres://toppqsvvpcgceh:8e560b0767dc6b30d5140589013a2baca8752165a642c8188459ca806176fa4c@ec2-54-243-252-91.compute-1.amazonaws.com:5432/da1ftjs8usjpu0')

def get_info(pid,url_from,path,article_type):
    soup = get_html(url_from)

    # maek title
    title = chs_to_cht(str(soup.title.string).replace('36','BIN '))

    # make content
    pcount = 0
    page_urls=[]
    for a_tag in soup.article.find_all('img'):
        pcount = pcount + 1
        url = [pcount,a_tag['src']]
        page_urls.append(url)
        a_tag['src'] = "../static/pic/"+pid+"_"+str(pcount)+".jpg"
        a_tag['class'] = "36img"
        del a_tag['width'],a_tag['height'],a_tag['sizes'],a_tag['srcset']
    
    tasks = [asyncio.ensure_future(download_img(pid,url[1],path,url[0],article_type)) for url in page_urls]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
    
    content = chs_to_cht(str(soup.article))
    content = content.replace('\r\n','<br>').replace('\u2028','').replace('\\\\','\\').replace('\\','').replace('\n','')

    #make scontent
    soup = BeautifulSoup(content, 'html.parser')
    for a_tag in soup.article.find_all('p'):
        if a_tag.string is not None and len(a_tag.string)>20 :
            scontent = a_tag.string
            break

    r = [title,content,scontent,pcount]

    engine.execute('INSERT INTO article (pid ,article_type ,url_from ,mode ,title ,content ,scontent ) VALUES (%s,%s,%s,%s,%s,%s,%s);',(pid ,article_type ,url_from ,'crawler' ,r[0] ,r[1] ,r[2]))



get_info('6','http://www.36dsj.com/archives/17187',os.path.join(os.getcwd()+'/app/static/pic'),'code')



