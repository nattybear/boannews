import bs4
import collections
import configparser
import urllib.request
import sqlite3

Article = collections.namedtuple("Article", "url title")

def work(raw):
  url = 'https://blog.alyac.co.kr' + raw.a['href']
  title = raw.strong.text
  return Article(url, title)

config = configparser.RawConfigParser()
config.read('.boannews.ini')

with urllib.request.urlopen(config['alyac']['url']) as f:
  st = f.read().decode()

soup = bs4.BeautifulSoup(st, 'html.parser')
raws = soup.find_all('div', {'id': 'content_article_rep'})
articles = map(work, raws)

con = sqlite3.connect('boannews.db')
cur = con.cursor()
sql = 'INSERT INTO boannews VALUES (?, ?, 0)'

for article in articles:
  try:
    cur.execute(sql, article)
    con.commit()
  except sqlite3.IntegrityError as e:
    pass

con.close()
