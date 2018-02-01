#!/usr/bin/python3

from db import insert
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
from datetime import datetime
from re import compile

url = 'http://asec.ahnlab.com/category'
f = urlopen(url)
b = f.read().decode('utf-8')
f.close()

s = bs(b, 'html.parser')
rows = s.ol.find_all('li')
records = []
p = compile('/(\d+)[?]')
for row in rows:
	link = row.a['href']
	title = row.a.string
	m = p.search(link)
	id = m.group(1)
	time = datetime.now().strftime('%Y.%m.%d %H:%M:%S')
	link = url[:22] + link
	record = (id, title, link, time)
	records.append(record)

insert(records, 'asec')
