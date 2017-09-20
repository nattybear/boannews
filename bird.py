#!/usr/bin/python3

from bs4 import BeautifulSoup
from urllib.request import urlopen
from time import strptime, strftime
from sqlite3 import connect, IntegrityError

f = urlopen('http://hummingbird.tistory.com/rss')
b = f.read()
f.close()

soup = BeautifulSoup(b, 'xml')

con = connect('news.db')
cur = con.cursor()

items = soup.find_all('item')
for item in items:
	title = item.title.string
	link = item.link.string
	date = item.pubDate.string
	date = strptime(date, "%a, %d %b %Y %H:%M:%S +0900")
	date = strftime("%Y.%m.%d %H:%M", date)
	t = (title, link, date)
	sql = 'insert into bird values (?,?,?)'
	try:
		cur.execute(sql, t)
	except IntegrityError as e:
		continue
con.commit()
con.close()
