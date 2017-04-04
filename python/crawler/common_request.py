# -*- coding: utf-8 -*-
# Created by Eli on 2017/4/2

import requests

def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "Gotten Error"

if __name__ == '__main__':
    url = "http://item.jd.com/10377022594.html"
    print(getHTMLText(url)[:1000])