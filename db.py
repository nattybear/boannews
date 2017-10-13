from sqlite3 import connect, IntegrityError

def insert(rows, table):
	con = connect('news.db')
	cur = con.cursor()

	for row in rows:
		size = len(row)
		sql = 'insert into %s values (%s)'
		q = ','.join('?' * size)
		sql = sql % (table, q)

		try:
			cur.execute(sql, row)
		except IntegrityError as e:
			print(e, row)

	con.commit()
	con.close()
