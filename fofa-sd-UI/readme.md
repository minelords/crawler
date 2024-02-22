## 这是一个爬取fofa资源来获取sdwebui链接的项目  

### 有以下这些功能  

### 1.info.py  
输入关键字，账号密码，获取fofa的信息，省去了api的花费  

### 2.sdapi.py  
通过获取的api执行ai的txt2img操作  

### 3.model.py  
爬取api所有的模型来供选择   

### 4.sdwebui_txt2img.ipynb  
利用第三方库sdwebuiapi来进行扩展  
并且还能通过colab来进一步减少本机的负担  
  
### 其他  
url.txt保存爬取的网站  
output保存生成的AI绘画照片  

### 最后   
我愿称这个项目为非常没有且无聊的铁公鸡一毛不拔且白嫖别人项目  
还有，sdwebui的fofa指纹为`fid="4OeA79EXS7Z+DdzkAvrBag==" && country="CN"`,CN自选  
鹰图和360夸克找不到指纹识别所以就用了fofa  
但是fofa貌似用cookie登陆有问题，最后选择了使用selenium登陆