import xml.etree.ElementTree as ET
import pickle
folder = './task'
dic = {}
files_per_task = 1
resfile = ET.parse('resroot.xml')
filename1 = ('hey','.xml')
filename2 = ('namaste','.xml')
filename3 = ('tumatmul','.xml')
filename4 = ('linpack','.xml')
filename5 = ('pi','.xml')
filename6 = ('cond_42_','.xml')
filename7 = ('cond_mod','.xml')

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


#length of one task is 9 nodes
def addNineZero(currentset):
	return currentset+[0]*9

def addNine(currentset,root):
	if root.tag == 'nono':
		return addNineZero(currentset)
	for elem in root.iter():
		if want(elem.tag):
			currentset.append(elem.text)
	return currentset

def removeNine(currentset):
	return currentset[:-9]

def getRoots(files_per_task, filename, path):
	#returns list of roots of all variations of a task
	roots = []
	roots.append(ET.Element('nono'))
	for i in range(files_per_task):
		currentPath = (path+filename[0]+str(i+1)+filename[1])
		tree = ET.parse(currentPath).getroot()
		for c in tree:
			#only has one child "periodictask"
			roots.append(c)
	
	return roots

type1 = getRoots(files_per_task = files_per_task,filename = filename1, path = folder+'1/')
type2 = getRoots(files_per_task = files_per_task,filename = filename2, path = folder+'2/')
type3 = getRoots(files_per_task = files_per_task,filename = filename3, path = folder+'3/')
type4 = getRoots(files_per_task = files_per_task,filename = filename4, path = folder+'4/')
type5 = getRoots(files_per_task = files_per_task,filename = filename5, path = folder+'5/')
type6 = getRoots(files_per_task = files_per_task,filename = filename6, path = folder+'6/')
type7 = getRoots(files_per_task = files_per_task,filename = filename7, path = folder+'7/')

ac = 0

#TODO need to figure out where to insert for to get 
for a in type1:
	taskset  = []
	resroot = ET.Element('taskset')
	aname = str(ac)
	ac+=1
	bc=0
	if a.tag !='nono':
		resroot.append(a)
	taskset = addNine(taskset,a)
	
	for b in type2:
		bname = str(bc)
		bc+=1
		cc=0
		if b.tag !='nono':
			resroot.append(b)
		taskset = addNine(taskset,b)
				
		for c in type3:
			cname = str(cc)
			cc+=1
			dc=0
			if c.tag!= 'nono':
				resroot.append(c)
			taskset = addNine(taskset,c)

			for d in type4:
				dname = str(dc)
				dc+=1
				ec=0
				if d.tag != 'nono':
					resroot.append(d)
				taskset = addNine(taskset,d)

				for e in type5:
					ename = str(ec)
					ec+=1
					fc=0
					if e.tag!='nono':
						resroot.append(e)
					taskset = addNine(taskset,e)

					for f in type6:
						fname = str(fc)
						fc+=1
						gc = 0
						if f.tag!='nono':
							resroot.append(f)
						taskset = addNine(taskset,f)

						for g in type7:
							gname = str(gc)
							gc+=1
							if g.tag!='nono':
								resroot.append(g)
							taskset = addNine(taskset,g)

							### cut t make if less types
							#creates filenames depending on the variation of the task in the set
							code = aname+bname+cname+dname+ename+fname+gname
							path = './sets/'+code
							path +='.xml'
							resfile._setroot(resroot)
							resfile.write(path)
							dic[code]=taskset[:]
							###cut to make if less files
							if g.tag!='nono':
								resroot.remove(g)
							taskset = removeNine(taskset)
						if f.tag!='nono':
							resroot.remove(f)
						taskset = removeNine(taskset)	
					if e.tag!='nono':
						resroot.remove(e)
					taskset = removeNine(taskset)
				if d.tag!='nono':
					resroot.remove(d)
				taskset = removeNine(taskset)
			if c.tag!='nono':
				resroot.remove(c)
			taskset = removeNine(taskset)
		if b.tag!='nono':
			resroot.remove(b)
		taskset = removeNine(taskset)

with open('data.pickle','wb') as f:
	pickle.dump(dic, f, -1)


print('this has been pickled')