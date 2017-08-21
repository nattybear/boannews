#!/usr/bin/python

from urllib import urlopen
from bs4 import BeautifulSoup
from re import compile
from sqlite3 import connect, IntegrityError
from time import sleep

def find_id(href):
	p = compile('etnews.com/(\d+)')
	m = p.search(href)
	return m.group(1)

url = 'http://www.etnews.com/news/section.html?id1=04'

fp = urlopen(url)
buf = fp.read()
fp.close()

soup = BeautifulSoup(buf, 'html.parser')

clearfixs = soup.find_all('dl')

con = connect('news.db')
c = con.cursor()

for i in clearfixs:
	
	try:

		if 'clearfix' in i['class'][0]:

			headline = i.dt.string
			url = i.dt.a['href']
			id = find_id(url)			
			reporter = i.find_all('span')[0].string
			time = i.find_all('span')[1].string

			t = (id, headline, reporter, time, url)

			c.execute("INSERT INTO etnews VALUES(?,?,?,?,?)", t) 

	except KeyError, e:
		pass

	except IntegrityError, e:
		pass

con.commit()
con.close()
