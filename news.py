from bottle import run, route, template, debug
from sqlite3 import connect

query = '''
SELECT headline, url, time from boannews
UNION
SELECT headline, url, time from dailysecu
UNION
SELECT headline, url, time from etnews
ORDER BY time DESC
'''

@route('/news')
def news_list():
	con = connect('news.db')
	c = con.cursor()
	c.execute(query)
	result = c.fetchall()
	c.close()
	output = template('make_table', rows=result)
	return output

debug(True)

run(host='0.0.0.0', reloader=True)
