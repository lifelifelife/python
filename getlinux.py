#! usr/bin/python
# -*-coding:utf-8-*-

import re

import urllib
import urllib2
import cookielib


def getHtml(url):
    # data = urllib.urlencode(values)
    # headers = {"User-agent": "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1"}
    # req = urllib2.Request(url, data, headers)
    # cj = cookielib.CookieJar()
    # opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    # response = opener.open(req)
    # html = response.read()
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
        print path
        if path == '/':
            continue
        if re.search('"*(.pdf|.rar|.zip|.txt|tar.gz)"', path):
            urls.append(path)
            continue

        newurl = golbalurl + path[1:]
        urls += getDownloadUrls(newurl)
    return urls

# data = {'username': 'www.linuxidc.com', 'passworld': 'www.linuxidc.com'}
golbalurl = 'http://linux.linuxidc.com/'
pathlist = getDownloadUrls(golbalurl)
print pathlist
