__author__ = 'liuguohao'
#coding=utf-8
#Python中通过urllib.unquote，解码出原始url地址

import  urllib.request;

encodedUrl = "http%3A%2F%2Fwww.baidu.com%2Fcache%2Fuser%2Fhtml%2Fjump.html"
decodedUrl = urllib.request.unquote(encodedUrl)
print("encodedUrl=\t%s\r\ndecodedUrl=\t%s"%(encodedUrl, decodedUrl))
#encodedUrl=     http%3A%2F%2Fwww.baidu.com%2Fcache%2Fuser%2Fhtml%2Fjump.html
#decodedUrl=     <a href="http://www.baidu.com/cache/user/html/jump.html">http://www.baidu.com/cache/user/html/jump.html</a>
