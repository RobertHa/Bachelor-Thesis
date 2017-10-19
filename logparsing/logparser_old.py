#!/usr/bin/env python3
import xml.etree.ElementTree as ET
#import pickle


"""

structure of a log file:

<profile>
	<events>
		<task id="0" foc_id="0" execution-time="0" priority="0" core="0" policy-id="0" state="0" arrival-time="0" start-time="0" exit-time="0" session="" thread="" ram_quota="0" ram_used="0"/>
		...
	</events>
</profiles>

"""

def getinfo(path):
	tasks = {}
	with open(path, 'r')as file:
		for line in file:
			if l == '</profile>\n' or l == '</profile>':
				return tasks
			l = line.split()
			if len(l)>1:
				typ = l[1].split('=')[1][1:-1]
				if typ != 'START':
					if typ != 'EXIT_ERROR':
						if typ != 'EXTERNAL':
							ID= l[2].split('=')[1][1:-1]
							tasks[str(ID)] = typ
						else:
							print('there was type EXTERNAL!!!!!!!!!!!!!!!!!!!!!')
					else:
						print('there was an exiterror!!!!!!!!!!!!!!!!!!!!!!!')		
	return tasks

def success(taskset):
	ret = True
	for t in taskset:
		ret = ret and t[0]=='EXIT'
	return ret

def getxmlinfo(path):
	taskset = []
	root = ET.parse(path).getroot()
	for events in root:
		for event in events:
			if event.attrib['type']!='START':
				taskset.append((event.attrib['type'],event.attrib['task-id']))
	return taskset
##############################################################
folder = ''#'/logparsing'

a_till = 2
b_till = 2
c_till = 2
d_till = 2
e_till = 2
f_till = 2
g_till = 2

a = 0
b = 0
c = 0
d = 0
e = 0
f = 0
g = 1

while a <types_per_task:
	while b < types_per_task:
		while c < types_per_task:
			while d < types_per_task:
				while e < types_per_task:
					while f < types_per_task:
						while g < types_per_task:
							name = str(a)+str(b)+str(c)+str(d)+str(e)+str(f)+str(g)
							print("taskset "+name)
							taskset = getinfo(folder+'log'+name+'.xml')
							print(taskset)
							print('set is a success:',success(taskset))

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

	