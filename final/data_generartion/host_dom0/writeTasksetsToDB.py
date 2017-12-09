import pickle
import sqlite3


def insert(dictionary, cursor, name):
	temp = dictionary[name]
	insert = [name]
	for e in temp:
	#	if e == '5M':
	#		insert.append(5)
	#	else:
		insert.append(int(e))
	cursor.execute('INSERT INTO tasksets VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',insert)

########################################################################
print("trying to open data.pickle")

with open('data.pickle', 'rb') as f:
	setinfo = pickle.load(f)

print('this has been unpickled')



database = sqlite3.connect('training_data.db')
db = database.cursor()
print("opened db")
#drop table if exists
db.execute('DROP TABLE IF EXISTS tasksets')
#create table
db.execute('''CREATE TABLE tasksets (id TEXT PRIMARY KEY , Task1_id INTEGER, Task1_criticaltime INTEGER, Task1_arg1 INTEGER, Task2_id INTEGER, Task2_criticaltime INTEGER, Task2_arg1 INTEGER, Task3_id INTEGER, Task3_criticaltime INTEGER, Task3_arg1 INTEGER, Task4_id INTEGER, Task4_criticaltime INTEGER, Task4_arg1 INTEGER, Task5_id INTEGER, Task5_criticaltime INTEGER, Task5_arg1 INTEGER, Task6_id INTEGER, Task6_criticaltime INTEGER, Task6_arg1 INTEGER, Task7_id INTEGER, Task7_criticaltime INTEGER, Task7_arg1 INTEGER)''')
print("created table")
for key in setinfo.keys():
	insert(dictionary = setinfo, cursor = db, name = key)

database.commit()
for n in db.execute('SELECT COUNT(*) from tasksets'):
	print("tablesize of tasksets:",n[0])

#for n in db.execute('SELECT COUNT(*) from success'):
#	print("tablesize of success:",n[0])

'''
for row in db.execute('SELECT * FROM tasksets ORDER BY id ASC LIMIT 5'):
	print(row)

for row in db.execute('SELECT * FROM tasksets ORDER BY id DESC LIMIT 5'):
	print(row)
'''
