from bs4 import BeautifulSoup
from urllib import urlopen
from sqlite3 import connect, IntegrityError
from re import compile
from time import sleep
from datetime import datetime

def find_idxno(href):
	p = compile('idxno=(\d+)')
	m = p.search(href)
	return m.group(1)	

while True:

	url = 'http://www.dailysecu.com/?mod=news&act=articleList&view_type=S&sc_code=1435901200'

	fp = urlopen(url)
	buf = fp.read()
	fp.close()

	con = connect('news.db')
	c = con.cursor()

	soup = BeautifulSoup(buf, 'html.parser')

	box = soup.find_all('div')

	for i in box:

		try:

			if i['class'][0] == 'box':

				url = 'http://www.dailysecu.com' + i.a['href']
				id = find_idxno(url)
				headline = i.ul.li.a.string
				reporter = i.find_all('span')[1].string.split(' ')[0]
				time = datetime.now().strftime('%Y.%m.%d %H:%M:%S')

				t = (id, headline, reporter, time, url)

				c.execute("INSERT INTO dailysecu VALUES (?,?,?,?,?)", t)

		except KeyError, e:
			pass

		except IntegrityError, e:
			pass

	con.commit()
	con.close()

	sleep(60 * 30)
