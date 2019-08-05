#!/usr/bin/env python
# -*- coding:utf-8 -*-
#美女图片提取
import requests
from  bs4  import  BeautifulSoup
import os
import time

#保存一个储存位置
save_path = 'E:/Photo'
#创建文件夹，判断是否存在
def crear_File(file_path):
    if os.path.exists(file_path) is False:
        os.mkdir(file_path)
    os.chdir(file_path)

#开始解析，提取
def start_one(url):
    headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                 'Chrome/75.0.3770.90 Safari/537.36'
                  'Opera/9.25 (Windows NT 5.1; U; en)'
                 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR '
                 '2.0.50727)'
}
    reponse = requests.get(url,headers=headers).content
    bs4 = BeautifulSoup(reponse,'lxml')
    html = bs4.find('div',class_='text_left text_leftbq').find_all('img')
    for i in html:
        b = i.attrs['src2']
        array = b.split('/')
        file_name = array[len(array) - 1]
        print("正在保存:" + file_name)
        g = requests.get(b,headers=headers)
        f = open(file_name,'wb')
        f.write(g.content)
        f.close()


def main(shuzi):
    url = 'http://sc.chinaz.com/tag_tupian/yazhoumeinv_' + str(shuzi)+'.html'
    start_one(url)
    crear_File(save_path)

#进行翻页，与时间设定
if __name__ == '__main__':
    for i in range(2,24):
        main(shuzi=i)
        time.sleep(1)
