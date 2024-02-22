# -*- coding:utf8 -*-
import requests
import re
from urllib import parse
import os
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

class ImageSpider(object):
    def __init__(self):
        self.url = 'https://maozidy.com/index.php/vod/show/id/20/page/{}.html'
        self. headers = {'User-Agent': f'{UserAgent().firefox}'}

    # 获取图片
    def get_image(self,url):
        #使用 requests模块得到响应对象
        res= requests.get(url,headers=self.headers)
        # 更改编码格式
        res.encoding="utf-8"
        # 得到html网页
        soup=BeautifulSoup(res.text,'html.parser')
        tag=soup.find_all("a",{"class":"fed-list-pics fed-lazy fed-part-2by3"})
        print(tag)
        tag1=soup.find_all("a",{"class":"fed-list-title fed-font-xiv fed-text-center fed-text-sm-left fed-visible fed-part-eone"})
        #正则解析
        pattern = re.compile(r'.*?data-original="(.*?)" href.*?>',re.S)
        img_link_list = pattern.findall(str(tag))
        #存储图片的url链接 
        print(img_link_list)

        # 保存列表
        for img_link,t1 in zip(img_link_list,tag1):
            name=t1.get_text()
            directory = 'D:\\002-Py\maozidy\img\{}.jpg'.format(name)
            # 如果目录不存在则创建，此方法常用
            filename = directory
            self.save_image(img_link,filename)

    #下载图片
    def save_image(self,img_link,filename):
        html = requests.get(url=img_link,headers=self.headers).content
        with open(filename,'wb') as f:
            f.write(html)
        print(filename,'下载成功')

    # 入口函数 
    def run(self):
        for i in range(1,200):
            url = self.url.format(i)
            self.get_image(url)

if __name__ == '__main__':
    spider = ImageSpider()
    spider.run()

