import sqlite3
import urllib.request
import xml.etree.ElementTree as ET

url = 'http://www.boannews.com/media/news_rss.xml?skind=5'
with urllib.request.urlopen(url) as f:
  s = f.read().decode('euc-kr')
root = ET.fromstring(s)
channel = root[0]
items = filter(lambda x: x.tag == 'item', channel)
con = sqlite3.connect('boannews.db')
cur = con.cursor()
sql = 'INSERT INTO boannews VALUES (?, ?, FALSE)'

for item in items:
  title = item[0].text.strip()
  url = item[1].text
  t = title, url
  try:
    cur.execute(sql, t)
    con.commit()
  except sqlite3.IntegrityError:
    pass

con.close()
