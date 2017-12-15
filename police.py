#!/usr/bin/python3

from db import insert
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
from datetime import datetime

url = 'http://cyberbureau.police.go.kr/board/boardList.do?board_id=all&page=1&mid=040501'
f = urlopen(url)
b = f.read().decode('utf-8')
f.close()

s = bs(b, 'html.parser')
rows = s.tbody.find_all('tr')[:-1]
records = []
for row in rows:
	td = row.find_all('td')
	id = td[0].string.replace('\r\n', '').strip()
	title = td[1].a.string
	link = url[:31] + td[1].a['href']
	writer = td[2].string
	enroll = td[3].string
	time = datetime.now().strftime('%Y.%m.%d %H:%M:%S')
	r = (id, title, link, writer, enroll, time)
	records.append(r)

insert(records, 'police')
