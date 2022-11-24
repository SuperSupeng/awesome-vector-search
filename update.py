# -*- coding: utf-8 -*-
import urllib3
from lxml import etree
import html
import re
import sys

urllib3.disable_warnings()

baseUrl = 'https://api.github.com/repos/'

def getToken():
    f=open('token.txt')
    for line in f:
        return line


def getUpdateTime(owner, repo):
    url = baseUrl + owner + '/' + repo + '/commits'
    print(url)
    http = urllib3.PoolManager()
    r = http.request('GET', url, headers = headers)
    print(r.status)
    print('返回结果：', r.data.decode('utf-8'))

def writeReadme():
    f = open('README_test.md', 'w+')

    head = """
    # awesome-vector-search

    <div align="center">
    <img border="0" src="https://camo.githubusercontent.com/54fdbe8888c0a75717d7939b42f3d744b77483b0/687474703a2f2f6a617977636a6c6f76652e6769746875622e696f2f73622f69636f2f617765736f6d652e737667" />
    <img border="0" src="https://camo.githubusercontent.com/1ef04f27611ff643eb57eb87cc0f1204d7a6a14d/68747470733a2f2f696d672e736869656c64732e696f2f7374617469632f76313f6c6162656c3d254630253946253843253946266d6573736167653d496625323055736566756c267374796c653d7374796c653d666c617426636f6c6f723d424334453939" />
    <a href="https://github.com/Unstructured-Data-Community/awesome-vector-search/issues">     <img border="0" src="https://img.shields.io/github/issues/Unstructured-Data-Community/awesome-vector-search" /> </a>
    <a href="https://github.com/Unstructured-Data-Community/awesome-vector-search/network/members">     <img border="0" src="https://img.shields.io/github/forks/Unstructured-Data-Community/awesome-vector-search" /> </a>
    <a href="https://github.comUnstructured-Data-Community/awesome-vector-search/stargazers">     <img border="0" src="https://img.shields.io/github/stars/Unstructured-Data-Community/awesome-vector-search" /> </a>
    </div>
    """

    f.write(head)
    f.close

if __name__ == "__main__":
    Authorization = 'Bearer ' + sys.argv[1]
    headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36', 'Accept': 'application/vnd.github+json', 'Authorization': Authorization} 

    getUpdateTime("milvus-io","milvus")

    