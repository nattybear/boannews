import sqlite3
import urllib.request
import bs4

url = 'https://www.boho.or.kr/data/secNoticeList.do'

with urllib.request.urlopen(url) as f:
  s = f.read().decode()

soup = bs4.BeautifulSoup(s, 'html.parser')
table = soup.select_one('.basicList')
body = table.tbody
rows = body.find_all('tr')

con = sqlite3.connect('boannews.db')
cur = con.cursor()
sql = 'INSERT INTO boannews VALUES (?, ?, FALSE)'

for row in rows:
  a = row.find('a')
  link = 'https://www.boho.or.kr' + a.get('href')
  title = a.text
  t = link, title
  try:
    cur.execute(sql, t)
    con.commit()
  except sqlite3.IntegrityError:
    pass

con.close()
