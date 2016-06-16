#! usr/bin/python
# -*-coding:utf-8-*-

import re

import urllib
import requests
import socket
import os

socket.setdefaulttimeout(30)


def getHtml(url):
    response = urllib.urlopen(url)
    html = response.read()
    return html


def getDownloadUrls(url):
    html = getHtml(url)
    regpath = '<a href="(.*?)">(?!\[To)'
    repath = re.compile(regpath, re.S | re.I)
    pathlist = re.findall(repath, html)
    urls = []
    for path in pathlist:
        if path == '/':
            continue
        if path.find('.pdf') > 0 or path.find('.rar') > 0 or path.find('.zip') > 0 or path.find('.tar.gz') > 0:
            if len(path.split('/')[-1]) > 0:
                try:
                    tra_str = urllib.unquote(path.split('/')[-1]).decode('utf-8')
                    local_filename = local_path + '/' + tra_str
                    filename, msg = urllib.urlretrieve(golbalurl + path[1:], local_filename)
                    print "local_filename", filename, msg
                except Exception, e:
                    urllib.urlcleanup()
                    print "load file failed", e

            continue
        newurl = golbalurl + path[1:]
        urls += getDownloadUrls(newurl)
    return urls


# def downloadFile(url, index):
#     local_filename = str(index)+"-"+url.split('/')[-1]
#     # NOTE the stream=True parameter
#     r = requests.get(url, stream=True)
#     with open(local_filename, 'wb') as f:
#         for chunk in r.iter_content(chunk_size=1024):
#             if chunk:  # filter out keep-alive new chunks
#                 f.write(chunk)
#                 f.flush()
#     return local_filename


def iota():
    n += 1
    return n

# data = {'username': 'www.linuxidc.com', 'passworld': 'www.linuxidc.com'}
golbalurl = 'http://linux.linuxidc.com/'
local_path = os.path.abspath('.')
local_path += '/doc'
pathlist = getDownloadUrls(golbalurl)
