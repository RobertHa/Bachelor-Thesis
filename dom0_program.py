#!/usr/bin/env python3

from dom0_client import *
from dom0_sql import *
import time

types_per_task = 2
types_per_task+=1

a = 0
b = 0
c = 0
d = 0
e = 0
f = 0
g = 1

counter = 1

session = Dom0_session('192.168.217.21', 3001)


print('Waiting for 10 seconds...')

session.read_tasks(script_dir + 'init.xml')
session.send_descs()
session.send_bins()
session.clear()

time.sleep(1)


while a <types_per_task:
	while b < types_per_task:
		while c < types_per_task:
			while d < types_per_task:
				while e < types_per_task:
					while f < types_per_task:
						while g < types_per_task:
							name = str(a)+str(b)+str(c)+str(d)+str(e)+str(f)+str(g)
							session.read_tasks(script_dir + 'sets/'+name+'.xml')
							print(str(counter)+': ',name+'.xml')	
							counter+=1
							session.send_descs()
							session.start()

							time.sleep(4)
							session.stop()

							time.sleep(1)
							session.profile(script_dir+'/log/log'+name+'.xml')
							
							session.clear()
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

print(a,b,c,d,e,f,g)

help()
code.interact(local=locals())
