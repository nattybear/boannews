from bottle import run, route, template, debug
from sqlite3 import connect

@route('/news')
def news_list():
	con = connect('news.db')
	c = con.cursor()
	c.execute(open('query.conf', 'rb').read())
	result = c.fetchall()
	c.close()
	output = template('make_table', rows=result)
	return output

debug(True)

run(host='0.0.0.0', reloader=True)
