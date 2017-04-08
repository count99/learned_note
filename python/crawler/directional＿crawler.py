# -*- coding: utf-8 -*-
# Created by Eli on 2017/4/8

import bs4, requests
from bs4 import BeautifulSoup

def getHTML(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print("ERROR!")

def getinfoFromHTML(html):
    get_list = []
    soup = BeautifulSoup(html, 'html.parser')
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr.find_all('td')
            get_list.append([tds[1].string, tds[2].string, tds[3].string])
    return get_list

if __name__ == '__main__':
    url = 'http://www.zuihaodaxue.com/zuihaodaxuepaiming2017.html'
    html = getHTML(url)
    get_list = getinfoFromHTML(html)
    tplt = "{0: ^15}\t{1: ^15}\t{2: ^15}"
    print(tplt.format('大學', '地區', '分數'))
    for i in get_list:
        print(tplt.format(i[0], i[1], i[2]))