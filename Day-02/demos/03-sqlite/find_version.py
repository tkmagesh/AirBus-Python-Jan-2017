import sqlite3 as lite
import sys

con = None

try:
	con = lite.connect('test.db')
	cur = con.cursor()
	cur.execute('select sqlite_version()')
	data = cur.fetchone()
	print('sqlite version = {}'.format(data))
except lite.Error, e:
	print 'something went wrong'
	sys.exit(1)
finally:
	if con:
		con.close()
