import requests,re,json
from bs4 import BeautifulSoup
import asyncio
from aiohttp import ClientSession
import time


#下載圖片
from io import StringIO,BytesIO
from PIL import Image

async def download_img(pid,url,path,pcount,article_type):
    image_name = pid+'_'+str(pcount)+'.jpg'
    async with ClientSession() as session:
        async with session.get(url) as resp:
            print(pcount)
            i = await resp.read()
            print(pcount,'read')
            with open(path+'/'+image_name,"wb") as f :
                f.write(i)


def download_img_1(pid,url,path,pcount,article_type):
    print('_1')
    image_name = pid+'_'+str(pcount)+'.jpg'
    i = requests.get(url)
    print('_1_1')
    with open(path+'/'+image_name,"wb") as f :
        f.write(i.content)


path = '../static/pic/news'
page_url_base = 'http://bigdatainsight.herokuapp.com/static/pic/code/4_'
page_urls = [[i,page_url_base+str(i)+'.jpg'] for i in range(1,6)]


tStart = time.time()#計時開始
tasks = [asyncio.ensure_future(download_img('10',url[1],path,url[0],'news')) for url in page_urls]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
tEnd = time.time()#計時結束
print("It cost %f sec" % (tEnd - tStart))#會自動做近位


tStart = time.time()#計時開始
for url in page_urls:
    download_img_1('11',url[1],path,url[0],'news')
tEnd = time.time()#計時結束
print("It cost %f sec" % (tEnd - tStart))#會自動做近位





