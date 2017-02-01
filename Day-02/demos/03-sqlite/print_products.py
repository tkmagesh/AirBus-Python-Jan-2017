import sqlite3 as lite
import sys

con = None
try:
	con = lite.connect('test.db')
	cur = con.cursor()
	cur.execute('select * from products')
	rows = cur.fetchall()
	#print rows
	for row in rows:
		print row
except lite.Error, e:
	print e
	sys.exit(1)
finally:
	if con:
		con.close()
