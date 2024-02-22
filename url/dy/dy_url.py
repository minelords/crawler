# -*- coding:utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
import requests
import time
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import re

# 配置代理
proxy = Proxy()
proxy.proxy_type = ProxyType.MANUAL
proxy.http_proxy = "http://localhost:2080"

# 创建 Chrome WebDriver 实例，并添加代理选项
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--proxy-server=http://localhost:2080")
chrome_options.add_argument('--headless')

# 创建 WebDriver
driver = webdriver.Chrome(options=chrome_options)
url="https://maozidy.com/index.php/vod/show/id/20/page/{}.html"
def get_detail(url):
    #响应头
    headers={
        'User-Agent': f'{UserAgent().Chrome}'
    }
    #目前网站暂时不需要代理
    """
    proxies = {
        'http': 'http://127.0.0.1:2080',
        'https': 'https://127.0.0.1:2080',
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
        dyurl=video_url(link,headers)
        video=name+":"+get_video(dyurl)
        with open("dy.txt","a") as f:
            f.write(video+"\n")


def video_url(link,headers):
        res=requests.get(url=link,headers=headers)
        soup=BeautifulSoup(res.text,'html.parser')
        tag=soup.find("a",{"class":"fed-deta-play fed-rims-info fed-btns-info fed-btns-green fed-col-xs4"})
        r_o=re.compile(r'.*?href="(.*?)">',re.S)
        r=r_o.findall(str(tag))
        return "https://maozidy.com"+r[0]

def get_video(url):
    # 打开网页
    # 替换为实际网页的 URL
    driver.get(url)

    # 等待页面加载（可根据实际情况调整）
    #time.sleep(3)

    network = driver.execute_script("return window.performance.getEntries();")
    for data in network:
        if data["name"].endswith("m3u8"):
            dy_url=data["name"][28:]
            return dy_url 
    driver.quit()

for i in range(1,200):
    newurl=url.format(i)
    get_detail(newurl)