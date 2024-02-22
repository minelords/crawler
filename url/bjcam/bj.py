import requests
from bs4 import BeautifulSoup
#import time
#import os 
from fake_useragent import UserAgent
import re

class Spider(object):
    def __init__(self):
        self.url=input('想要的视频url：')#视频API
        

    def get_video_url(self,url):
        headers = {'User-Agent': f'{UserAgent().edge}'}
        proxy={
        "https": "127.0.0.1:2080",
        "http": "127.0.0.1:2080"
     }
        res=requests.get(url=url,headers=headers,proxies=proxy)
        soup = BeautifulSoup(res.text, "html.parser")
        iframes = soup.find_all('iframe')
        for iframe in iframes:
            print(iframe)
        pattern=re.compile(r'<iframe.*?src="(.*?)".*?></iframe>',re.S)
        r_list=pattern.findall(str(iframe))
        for r in r_list:
            print(r)

    def run(self):
        url=self.url
        self.get_video_url(url)
    """    
    def run(self):
        directory=input("请输入链接保存目录:")
        # 如果目录不存在则创建，此方法常用
        if not os.path.exists(directory):
            os.makedirs(directory)
        filename="{}No{}.txt".format(directory, i)
    """

if __name__=='__main__':
    spider=Spider()
    spider.run()