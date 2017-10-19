#!/usr/bin/env python3
#import xml.etree.ElementTree as ET
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


##############################################################
folder = ''#'/logparsing'
for i in range(1,7):
	name = 'cond_mod'
	print("taskset "+str(i))
	#profile = ET.parse(folder+name+str(i)+'.xml').getroot()


	tasks = getinfo(folder+name+'profile'+str(i)+'.xml')
	#print(tasks)

	success = True
	for k in list(tasks.keys()):
		success = success and (tasks[k]=='EXIT')
	if success:
		print('this taskset is good')
	else:
		print('this set wont work')


	