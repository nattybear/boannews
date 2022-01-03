import collections
import configparser
import email.mime.text
import email.utils
import smtplib
import sqlite3

config = configparser.ConfigParser()
config.read('.boannews.ini')

con = sqlite3.connect('boannews.db')
cur = con.cursor()
sql = 'SELECT title, url FROM boannews WHERE sent = FALSE'
rows = list(cur.execute(sql))
Item = collections.namedtuple('Item', 'title, url')
items = map(Item._make, rows)

server = smtplib.SMTP_SSL(config['server']['host'])
server.login(config['server']['user'], config['server']['password'])

for item in items:
  content = '<a href="%s">원본 링크</a>' % item.url
  msg = email.mime.text.MIMEText(content, 'html')
  msg['Subject'] = item.title
  sender = config['sender']['name'], config['sender']['address']
  receiver = config['receiver']['name'], config['receiver']['address']
  msg['From'] = email.utils.formataddr(sender)
  msg['To'] = email.utils.formataddr(receiver)
  server.send_message(msg)
  sql = 'UPDATE boannews SET sent = TRUE WHERE url = ?'
  cur.execute(sql, (item.url,))
  con.commit()

server.quit()
con.close()
