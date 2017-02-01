import sqlite3 as lite
import sys

con = None
try:
	con = lite.connect('test.db')
	cur = con.cursor()
	#cur.execute('create table products(id int, name Text, cost numeric, units int)')
	cur.execute("insert into products values(?,?,?,?)", (1, 'pen', 10.0, 100))
	cur.execute("insert into products values(:id, :name, :cost, :units)", {"id" : 1, "name" : "pen", "cost" : 10, "units" : 100})
	cur.execute("insert into products values(2, 'pencil', 5.0, 200)")
	cur.execute("insert into products values(3, 'Marker', 50.0, 50)")
	cur.execute("insert into products values(4, 'Scribble Pad', 20.0, 20)")
	con.commit()
except lite.Error, e:
	print e
	sys.exit(1)
finally:
	if con:
		con.close()
