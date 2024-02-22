import json
import requests
import io
import base64
from PIL import Image, PngImagePlugin
import os
import time

def save_file():
    # 获取当前工作目录
    current_working_directory = os.getcwd()
    #相对路径
    relative_path="output"
    #完整路径
    full_path = os.path.join(current_working_directory, relative_path)
    if not os.path.exists(full_path):
        os.makedirs(full_path)

    # 获取当前时间戳（秒）
    timestamp = int(time.time())
    # 使用时间戳来命名一个文件
    filename = f"{timestamp}.png"
    file_path = os.path.join(full_path, filename)
    return file_path

os.environ["http_proxy"] = "http://127.0.0.1:2080"
os.environ["https_proxy"] = "http://127.0.0.1:2080"

url = "http://119.xxxxx.95:8001"

payload = {
    "prompt": "photo of beautiful age 18 girl, blonde hair, sexy, beautiful, naked, perfect breasts, big boobs, nipples, dslr, 8k, 4k, cinematic film still, natural skin, textured skin, outdoors, snow,",
    "negative_prompt":"text, watermark, low quality, medium quality, blurry, censored, wrinkles, deformed, mutated text, watermark, low quality, medium quality, blurry, censored, wrinkles, deformed, mutated",
    "steps": 20,
    "sampler_name": "DPM++ SDE Karras",
    "width": 480,
    "height": 640,
    "restore_faces": True
}

# 切换模型

override_settings = {}
override_settings["sd_model_checkpoint"] = "dreamshaperXL_turboDpmppSDE"
override_payload = {
                "override_settings": override_settings
            }
payload.update(override_payload)

response = requests.post(url=f'{url}/sdapi/v1/txt2img', json=payload)

r = response.json()

#保存图片
for i in r['images']:
    image = Image.open(io.BytesIO(base64.b64decode(i.split(",",1)[0])))

    png_payload = {
        "image": "data:image/png;base64," + i
    }
    response2 = requests.post(url=f'{url}/sdapi/v1/png-info', json=png_payload)

    pnginfo = PngImagePlugin.PngInfo()
    pnginfo.add_text("parameters", response2.json().get("info"))
    file_path=save_file()
    image.save(file_path, pnginfo=pnginfo)

