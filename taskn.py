#!/usr/bin/env python3

from dom0_client import *
from dom0_sql import *
import time

session = Dom0_session('192.168.217.21', 3001)
name = 'hey'


print('Waiting for 10 seconds...')
#i=0
#while i<1:
#session.live(script_dir +'log/' + 'log.xml')
time.sleep(3)
#	i=i+1

for x in range(1,2):
	session.read_tasks(script_dir + 'sets/'+name+str(x)+'.xml')
	print(name+str(x)+'.xml')	
	session.send_descs()
	session.send_bins()
	#session.live(script_dir +'log/' + 'log'+str(x)+'start.xml')
	session.start()

	#session.live(script_dir +'log/' + 'log'+str(x)+'run.xml')

	#time.sleep(1)

	#session.live(script_dir +'log/' + 'log'+str(x)+'run2.xml')
	#time.sleep(2)
	#session.live(script_dir +'log/' + 'log'+str(x)+'run3.xml')
	#time.sleep(3)

	#session.live(script_dir +'log/' + 'log'+str(x)+'run4.xml')
	time.sleep(10)
	session.stop()

	#session.live(script_dir + 'log/' +'log'+str(x)+'stop.xml')
	time.sleep(3)

	#session.live(script_dir +'log/' + 'log'+str(x)+'stop2.xml')
	session.profile(script_dir+'/log/'+name+'profile'+str(x)+'.xml')

	session.clear()





#session.profile(script_dir + 'log.xml')
#xml2sql(script_dir + 'log.xml', script_dir + 'dom0.db')

help()
code.interact(local=locals())
