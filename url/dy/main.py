import requests
import time
import csv
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import re

class Dy:
    def __init__(self):
        self.url='https://maozidy.com/index.php/vod/show/id/20/page/{}.html'

    def get_detail(self,url):
        #响应头
        headers={
            'User-Agent': f'{UserAgent().firefox}'
        }
        #目前网站暂时不需要代理
        """
        proxies = {
            'http': 'http://127.0.0.1:2080',
            'https': 'http://127.0.0.1:2080',
        }
        """
        res=requests.get(url=url,headers=headers)
        soup=BeautifulSoup(res.text,'html.parser')
        #电影名称及链接
        tag1=soup.find_all("a",{"class":"fed-list-title fed-font-xiv fed-text-center fed-text-sm-left fed-visible fed-part-eone"})
        #演员名
        tag2=soup.find_all("span",{"class":"fed-list-desc fed-font-xii fed-visible fed-part-eone fed-text-muted fed-hide-xs fed-show-sm-block"})
        
        for t1,t2 in zip(tag1,tag2):
            r_o=re.compile(r'.*?href="(.*?)">',re.S)
            r=r_o.findall(str(t1))
            link="https://maozidy.com"+r[0] #链接
            name=t1.get_text() #电影名
            actor=t2.get_text() #演员名
            dyurl=self.video_url(link,headers)
            print(dyurl)
            #self.save_detail(link,name,actor)
        
    def video_url(self,link,headers):  #具体电影位置
        res=requests.get(url=link,headers=headers)
        soup=BeautifulSoup(res.text,'html.parser')
        tag=soup.find("a",{"class":"fed-deta-play fed-rims-info fed-btns-info fed-btns-green fed-col-xs4"})
        r_o=re.compile(r'.*?href="(.*?)">',re.S)
        r=r_o.findall(str(tag))
        return "https://maozidy.com"+r[0]   

    def save_detail(self,link,name,actor): #csv保存详细信息
        with open("dy.csv", "a", encoding='utf-8-sig', newline="") as f:
            writer=csv.writer(f)
            actor=actor.replace("\r", "").replace("\n", "")
            L=[link,name,actor]
            writer.writerow(L)

    def run(self):
        for i in range(1,200):
            url=self.url.format(i)
            self.get_detail(url)
            time.sleep(1)
            
if __name__=="__main__":
    dy=Dy()
    dy.run()
