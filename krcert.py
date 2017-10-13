#!/usr/bin/python3

from db import insert
from net import getSrc
from bs4 import BeautifulSoup
from datetime import datetime

url_base = 'https://www.krcert.or.kr'

buffer = getSrc(url_base + '/main.do')

soup = BeautifulSoup(buffer, 'html.parser')

divs = soup.find_all('div')

for div in divs:
	try:
		if div['id'] == 'totalNewsPC':
			break
	except:
		pass

lis = div.find_all('li')

rows = []

for li in lis:
	url = url_base + li.a['href']
	id = url.split('=')[-1]
	title = ''
	time = datetime.now().strftime('%Y.%m.%d %H:%M:%S')
	for s in li.a.strings: title += s
	title = title.strip()
	t = id, title, time, url
	rows.append(t)

insert(rows, 'krcert')
