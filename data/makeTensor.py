import sys
import xml.etree.ElementTree as ET
import pickle

"""
all tags of a taskfile
want:
		don't want:
		taskset \n
		periodictask \n
id z
executiontime z
criticaltime z
		ucfirmrt 'none'
		uawmean \n
size z
priority z
period z
offset z
quota 5M
		pkg 'name'
		config \n
arg1 z
"""
"""
def want(name):
	return {
	'taskset': False,
	'periodictask': False,
	'id': True,
	'executiontime': True,
	'criticaltime': True,
	'ucfirmrt': False,
	'uawmean': False,
	'size':True,
	'priority':True,
	'period':True,
	'offset':True,
	'quota': True, #not sure if this should be in
	'pkg':False,
	'config':False,
	'arg1':True
	}[name] 
dic = {}
root = ET.parse(sys.argv[1]).getroot()
c = []
for elem in root.iter():
	if want(elem.tag):
		c.append(elem.text)
dic["1000000"]=c
print(dic["1000000"])

with open('test.pickle','wb') as f:
	pickle.dump(dic, f, -1)

"""
print('this has been unpickled')

with open('test.pickle', 'rb') as f:
	other = pickle.load(f)

print(list(other.keys()))
