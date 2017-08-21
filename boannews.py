#!/usr/bin/python

from urllib import urlopen
from bs4 import BeautifulSoup
from sqlite3 import connect, IntegrityError
from re import compile
from time import sleep

def href2idx(href):
	p = compile('idx=(\d+)')	
	m = p.search(href)
	return int(m.group(1))


url = 'http://boannews.com/media/t_list.asp?kind=0'

fp = urlopen(url)
buf = fp.read()
fp.close()

soup = BeautifulSoup(buf, 'html.parser')

lists = soup.find_all('div')

con = connect('news.db')
c = con.cursor()

for i in lists:

	try:

		if i['class'][0] == 'news_list':
			spans = i.find_all('span')

			href = i.a['href']
			
			id = href2idx(href)
			headline = spans[0].string
			reporter = spans[1].string.split(' | ')[0].split(' ')[0]
			time = spans[1].string.split(' | ')[1]
			url = 'http://boannews.com' + i.a['href']

			t = (id, headline, reporter, time, url)

			c.execute("INSERT INTO boannews VALUES(?,?,?,?,?)", t)

	except KeyError, e:
		pass

	except IntegrityError, e:
		pass

con.commit()
con.close()
