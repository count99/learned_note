# -*- coding: utf-8 -*-
# Created by Eli on 2017/4/5

import requests
import os

url = "http://image.nationalgeographic.com.cn/2017/0404/20170404040700260.jpg"
root = "/Users/eli/Documents/pics/"
path = root + url.split("/")[-1]

try:
    if not os.path.exists(root):
        os.makedirs(root)
    if not os.path.exists(path):
        r = requests.get(url)
        with open(path,"wb") as f:
            f.write(r.content)
            print ("文件保存成功")
    else:
        print("文件已存在")
except:
    print("爬取失敗")
