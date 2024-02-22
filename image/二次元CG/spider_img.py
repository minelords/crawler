import requests
import time
import os 
from fake_useragent import UserAgent
from PIL import Image
from io import BytesIO

class Spider(object):
    def __init__(self):
        self.url='http://2091y482x3.zicp.fun:222/img/wallpaper-api.php' #图片API
        self.name=input("选择图片的格式：")

    def get_final_url(self,url):
        self.headers = {'User-Agent': f'{UserAgent().firefox}'}
        res=requests.head(url,allow_redirects=True) #重定向到的URL
        final_url=res.url
        return final_url
    
    def save_image(self,url,filename):
        html=requests.get(url=url,headers=self.headers).content
        img_data = BytesIO(html)
        # 打开JPEG图像
        with Image.open(img_data) as img:
        # 将图像转换为WebP格式
            data = BytesIO()
            img.save(data, format=f"{self.name}")
        #将图像进行保存
        with open(filename, "wb") as f:
            f.write(data.getvalue())
            print(filename,"下载成功")
        
    def run(self):
        directory=input("请输入图片保存目录:")
        # 如果目录不存在则创建，此方法常用
        if not os.path.exists(directory):
            os.makedirs(directory)
        for i in range(1,100):
            time.sleep(0.1)
            filename="{}No{}.{}".format(directory, i,self.name)
            finurl=self.get_final_url(self.url)
            self.save_image(finurl,filename)

if __name__=='__main__':
    spider=Spider()
    spider.run()