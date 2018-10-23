# -*- coding: utf-8 -*-
'''
post
'''
import requests
import re
from bs4 import BeautifulSoup
import random
    
def md5jiemi(text):
    header  =  {
                "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                "Accept-Encoding":"gzip, deflate",
                "Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8",
                "Cache-Control":"max-age=0",
                "Connection":"keep-alive",
                "Content-Type":"application/x-www-form-urlencoded",
#                 "Cookie":"_ga=GA1.2.1134913203.1534906206; _gid=GA1.2.933581216.1534906206; mailplanBAK=R2555567727; mailplanD=R3248004911; _gat=1",
                "Host":"md5decrypt.net",
                "Origin":"http://md5decrypt.net",
                "Referer":"http://md5decrypt.net/en/",
                "Upgrade-Insecure-Requests":"1",
                "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
    }   
    path = ""
    url = "http://md5decrypt.net/en/" + path #接口
    payload  = "hash=" + text + "&" + str(random.randint(1,123987)) + "=&decrypt=Decrypt"
    
    r = requests.post(url, data=payload,  headers=header)
    
    s = BeautifulSoup(r.text,"lxml") #    soup = BeautifulSoup(r.text) bs4解析

    try:
        md5DecodeRslt = s.b.string  #获取<b></b>标签内的内容
#         print (md5DecodeRslt)
    except Exception:
        md5DecodeRslt ='暂未收录，1小时后再试~'
    return md5DecodeRslt
 
# text = "81dc9bdb52d04dc20036dbd8313ed055"
# http_request(text)


