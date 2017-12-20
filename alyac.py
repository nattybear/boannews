#!/usr/bin/python3

from net import getSrc
from db import insert
from urllib.parse import quote
from bs4 import BeautifulSoup as bs
from re import compile
from datetime import datetime

dir = quote('악성코드 분석 리포트')
url = 'http://blog.alyac.co.kr/category/' + dir
src = getSrc(url)

s = bs(src, 'html.parser')
rows = []
for li in s.ol.find_all('li'):
	for s in li.stripped_strings:
		title = s
		break
	dir = li.a['href']
	id = dir.split('?')[0][1:]
	link = url[:23] + dir
	time = datetime.now().strftime('%Y.%m.%d %H:%M:%S')
	row = id, title, link, time
	rows.append(row)

insert(rows, 'alyac')
