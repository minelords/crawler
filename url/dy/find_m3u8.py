# -*- coding:utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
import time

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
url = 'https://maozidy.com/index.php/vod/play/id/183862/sid/1/nid/1.html'
def get_video(url):
    # 打开网页
      # 替换为实际网页的 URL
    driver.get(url)

    # 等待页面加载（可根据实际情况调整）
    time.sleep(3)

    network = driver.execute_script("return window.performance.getEntries();")
    for data in network:
        if data["name"].endswith("m3u8"):
            dy_url=data["name"]
            return dy_url  
    driver.quit()

print(get_video(url))