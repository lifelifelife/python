#! usr/bin/python
# -*-coding:utf-8-*-

import re

import urllib
import requests


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
        if path == '/':
            continue
        if path.find('.pdf') > 0 or path.find('.rar') > 0 or path.find('.zip') > 0 or path.find('.tar.gz') > 0:
            urls.append(path)
            continue
        newurl = golbalurl + path[1:]
        urls += getDownloadUrls(newurl)
    return urls


def downloadFile(url, index):
    local_filename = str(index)+"-"+url.split('/')[-1]
    # NOTE the stream=True parameter
    r = requests.get(url, stream=True)
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:  # filter out keep-alive new chunks
                f.write(chunk)
                f.flush()
    return local_filename


# data = {'username': 'www.linuxidc.com', 'passworld': 'www.linuxidc.com'}
golbalurl = 'http://linux.linuxidc.com/'
pathlist = getDownloadUrls(golbalurl)
n = 0
for path in pathlist:
    print "loadfile:", path.split('/')[-1]
    downloadFile(golbalurl + path, n)
    n += 1
