import sqlite3

def getinfo(path, name, flaged):
	tasks = 0;
	for c in name:
		if c != "0":
			tasks = tasks + 1
	
	with open(path, 'r')as file:
		for line in file:
			if line == '</profile>\n' or line == '</profile>':
				if tasks != 0:
					flaged.append(name);
				return True
				
			l = line.split()
			if len(l)>1:
				typ = l[1].split('=')[1][1:-1]
				if typ != 'START':
					if typ != 'EXIT_ERROR':
						if typ == 'EXIT_EXTERNAL':
							#print('there was type EXIT_EXTERNAL!!!!!!!!!!!!!!!!!!!!!',path)
							if tasks != 0:
								flaged.append(name);
							return False
						if typ == 'EXIT_CRITICAL':
							#print('there was type EXIT_CRITICAL!!!!!!!!!!!!!!!!!!!!!',path)
							if tasks != 0:
								flaged.append(name);
							return False
					else:
						print('there was an EXIT_ERROR!!!!!!!!!!!!!!!!!!!!!!!',path)		
						if tasks != 0:
							flaged.append(name);
						return False
				else:
					tasks = tasks -1


def success(taskset):
	ret = True
	for t in taskset:
		ret = ret and t[0]=='EXIT'
	return ret



#########################################################################
folder = './log/'

a_till = 5
b_till = 5
c_till = 5
d_till = 5
e_till = 5
f_till = 5
g_till = 5

a = 0
b = 0
c = 0
d = 0
e = 0
f = 0
g = 1

flaged =[]
notFound = []
works = {}
dont = {}
t = 0
fa = 0
database = sqlite3.connect('training_data.db')
db = database.cursor()

print("opened db")

#drop table if exists
db.execute('DROP TABLE IF EXISTS success')
#create table
db.execute('''CREATE TABLE success(id TEXT PRIMARY KEY, succ INTEGER, fail INTEGER)''')


suc_counter = 0

while a <a_till:
	while b < b_till:
		while c < c_till:
			while d < d_till:
				while e < e_till:
					while f < f_till:
						while g < g_till:
							name = str(a)+str(b)+str(c)+str(d)+str(e)+str(f)+str(g)
							try:
								if getinfo(folder+'log'+name+'.xml', name, flaged):
									db.execute('INSERT INTO success VALUES(?,?,?)',[name,1,0])
									suc_counter = suc_counter +1
								else:
									db.execute('INSERT INTO success VALUES(?,?,?)',[name,0,1])
							except FileNotFoundError:
								notFound.append(name)
							g+=1
						g = 0
						f+=1
					f = 0	
					e+=1
				e = 0
				d+=1
			d = 0	
			c+=1
		c = 0	
		b+=1
	b = 0
	a+=1

print("flaged: ", flaged)


db.execute('DROP TABLE IF EXISTS flaged')
#create table
db.execute('''CREATE TABLE flaged(id TEXT PRIMARY KEY)''')
for n in flaged:
	db.execute('INSERT INTO flaged VALUES(?)',[n])

db.execute('DROP TABLE IF EXISTS notFound')
db.execute('''CREATE TABLE notFound(id TEXT PRIMARY KEY)''')
for i in notFound:
	db.execute('INSERT INTO notFound VALUES(?)',[i])

database.commit()

for n in db.execute('SELECT COUNT(*) from success'):
	print("tablesize of success:",n[0])
print(suc_counter, 'were successful')
for n in db.execute('SELECT COUNT(*) from notFound'):
	print("tablesize of notFound:",n[0])
'''
for row in db.execute('SELECT * FROM success ORDER BY id ASC LIMIT 5'):
	print(row[0],row[1:])

for row in db.execute('SELECT * FROM success ORDER BY id DESC LIMIT 5'):
	print(row[0],row[1:])
'''
