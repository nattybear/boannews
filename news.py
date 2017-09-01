#!/usr/bin/python3

from bottle import run, route, template, debug, redirect, request
from sqlite3 import connect

@route('/news')
def news_list():
	con = connect('news.db')
	c = con.cursor()
	c.execute(open('query.conf').read())
	result = c.fetchall()
	c.close()
	output = template('make_table', rows=result)
	return output

@route('/news/simple')
def news_list_simple():
	con = connect('news.db')
	c = con.cursor()
	c.execute(open('simple_query.conf').read())
	result = c.fetchall()
	c.close()
	output = template('simple_make_table', rows=result)
	return output

@route('/')
def home():
	ua = request.headers.get('User-Agent')
	if 'Android' in ua:
		redirect('/news/simple')
	elif 'iPhone' in ua:
		redirect('/news/simple')
	else:
		redirect('/news')

#debug(True)

run(host='0.0.0.0', port=80, reloader=True)
