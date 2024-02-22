import requests  
import json
import re
import time
  
url =  "https://stablediffusionapi.com/api/v3/text2img"  
  
payload = json.dumps({  
"key":  "your api key",  
"lora_model": "yae-miko-genshin",
  "prompt": "genshin_impact, crystalfly_(genshin_impact), yae_miko, kusunokinawate, 1girl, animal_ears, bangs, breasts, cherry_blossoms, cowboy_shot, detached_sleeves, earrings, falling_petals, floating_hair, floppy_ears, floral_print, flower_knot, fox_ears, hair_between_eyes, hair_ornament, hand_up, japanese_clothes, jewelry, long_hair, long_sleeves, looking_at_viewer, medium_breasts, nontraditional_miko, petals, purple_eyes, red_skirt, ribbon_trim, shirt, sidelocks, skirt, sleeveless, sleeveless_shirt, solo, tassel, thighs, turtleneck, white_sleeves, wide_sleeves",
  "negative_prompt": "bright lantern, brightness, (nipples:1.2), pussy, EasyNegative, (worst quality:2), (low quality:2), (normal quality:2), lowres, normal quality, ((monochrome)), ((grayscale)), skin spots, acnes, skin blemishes, age spot, glans,extra fingers, fewer fingers, strange fingers, bad hand, bare thighs",
  "width": "512",
  "height": "512",
  "samples": "1",
  "num_inference_steps": "30",
  "seed": None,
  "guidance_scale": 7.5,
  "webhook": None,
  "track_id": None
})  
  
headers =  {  
'Content-Type':  'application/json'  
}  

proxies = {
            'http': 'http://127.0.0.1:2080',
            'https': 'http://127.0.0.1:2080',
}
  
response = requests.request("POST", url, headers=headers, data=payload,proxies=proxies).text  
print(response)  
def save_img(text):
    pattern=re.compile(r'output":\["(.*?.png)"',re.S)
    r=pattern.findall(text)
    url=r[0].replace("\\","")
    img=requests.get(url,proxies=proxies).content
    filename="文件夹绝对地址"+str(int(time.time()))+".png"
    with open(filename,"wb") as f:
        f.write(img)
    print(filename+"下载成功！")

save_img(response)