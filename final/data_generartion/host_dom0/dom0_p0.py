#!/usr/bin/env python3
import sys
from dom0_client import *
from ANN import *
import time


types_per_task =4 
types_per_task+=1
vm = sys.argv[2]
progress = ""
progress_path = script_dir+"../../output/progress"+vm+".log"
with open(progress_path, 'r+')as o:
	progress = str(o.read())
	

start = progress
end = sys.argv[3]
#print('start:',start,'ende:',end)
a = int(start[0])
b = int(start[1])
c = int(start[2])
d = int(start[3])
e = int(start[4])
f = int(start[5])
g = int(start[6])

atill = int(end[0])
btill = int(end[1])
ctill = int(end[2])
dtill = int(end[3])
etill = int(end[4])
ftill = int(end[5])
gtill = int(end[6])

counter = 1
ip = sys.argv[1]
try:
	session = Dom0_session(ip, 3001)
except socket_error as serr:
	if serr.errno != errno.ECONNREFUSED:
		raise serr
	else:
		time.sleep(5)
		session = Dom0_session(ip,3001)

print('lets begin')

session.read_tasks(script_dir + 'init.xml')
session.send_descs()
session.send_bins()
session.clear()

time.sleep(1)


while a<=atill:
	while b <=btill:
		while c <=ctill:
			while d <=dtill:
				while e <=etill:
					while f <=ftill:
						while g <=gtill:
							name = str(a)+str(b)+str(c)+str(d)+str(e)+str(f)+str(g)
							session.read_tasks(script_dir + 'sets/'+name+'.xml')
							print('file '+str(counter)+' on ip '+ip+': ',name+'.xml')	
							temp = ""+name
							with open(progress_path, 'r+')as o:
								o.seek(0)
								o.write(temp)
								o.truncate()
							counter+=1
							session.send_descs()
							session.start()

							time.sleep(20)
							session.clear()

							time.sleep(1)
							session.profile(script_dir+'/log/log'+name+'.xml')
							
							
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

print('finished',start, 'till',end,'on ip:',ip)

with open(progress_path, 'r+')as o:
	o.seek(0)
	o.write("done")
	o.truncate()
