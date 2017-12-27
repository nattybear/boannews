#!/usr/bin/python3

from db import insert
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
from datetime import datetime

url = 'https://www.hauri.co.kr/security/issue.html'
f = urlopen(url)
b = f.read().decode('utf-8')
f.close()

s = bs(b, 'html.parser')
div = s.find_all('div')
tags = []
for d in div:
	try:
		c = d['class']
	except KeyError:
		continue
	if c[0] == 'bbs-list-row':
		tags.append(d)

rows = []
for t in tags:
	div = t.find_all('div')
	id = div[0].string
	link = div[1].a['href']
	title = div[2].strong.string
	enroll = div[3].string
	time = datetime.now().strftime('%Y.%m.%d %H:%M:%S')
	row = (id, title, link, enroll, time)
	rows.append(row)

insert(rows, 'hauri')
