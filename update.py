# -*- coding: utf-8 -*-
import urllib3
from lxml import etree
import html
import re

baseUrl = 'https://api.github.com/repos/OWNER/REPO/commits'
# https://docs.github.com/cn/rest/commits/commits

headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'} 

f = open('README.md', 'w+')
f.write('# awesome-vector-search\n')
f.close 