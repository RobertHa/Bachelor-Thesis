import xml.etree.ElementTree as ET

folder = './task'
liste = []
files_per_task = 2
resfile = ET.parse('resroot.xml')
filename1 = ('hey','.xml')
filename2 = ('namaste','.xml')
filename3 = ('tumatmul','.xml')
filename4 = ('linpack','.xml')
filename5 = ('pi','.xml')
filename6 = ('cond_42_','.xml')
filename7 = ('cond_mod','.xml')


def getRoots(files_per_task, filename, path):
	liste = []
	liste.append(ET.Element('nono'))
	for i in range(files_per_task):
		thisone = (path+filename[0]+str(i+1)+filename[1])
		tree = ET.parse(thisone).getroot()
		for c in tree:
			liste.append(c)
	
	return liste

type1 = getRoots(files_per_task = files_per_task,filename = filename1, path = folder+'1/')
type2 = getRoots(files_per_task = files_per_task,filename = filename2, path = folder+'2/')
type3 = getRoots(files_per_task = files_per_task,filename = filename3, path = folder+'3/')
type4 = getRoots(files_per_task = files_per_task,filename = filename4, path = folder+'4/')
type5 = getRoots(files_per_task = files_per_task,filename = filename5, path = folder+'5/')
type6 = getRoots(files_per_task = files_per_task,filename = filename6, path = folder+'6/')
type7 = getRoots(files_per_task = files_per_task,filename = filename7, path = folder+'7/')

ac = 0

for a in type1:
	resroot = ET.Element('taskset')
	aname = str(ac)
	ac+=1
	bc=0
	if a.tag !='nono':
		resroot.append(a)
	for b in type2:
		bname = str(bc)
		bc+=1
		cc=0
		if b.tag !='nono':
			resroot.append(b)
		
		for c in type3:
			cname = str(cc)
			cc+=1
			dc=0
			if c.tag!= 'nono':
				resroot.append(c)

			for d in type4:
				dname = str(dc)
				dc+=1
				ec=0
				if d.tag != 'nono':
					resroot.append(d)

				for e in type5:
					ename = str(ec)
					ec+=1
					fc=0
					if e.tag!='nono':
						resroot.append(e)

					for f in type6:
						fname = str(fc)
						fc+=1
						gc = 0
						if f.tag!='nono':
							resroot.append(f)

						for g in type7:
							gname = str(gc)
							gc+=1
							if g.tag!='nono':
								resroot.append(g)

							### cut t make if less types
							name = './sets/'+aname+bname+cname+dname+ename+fname+gname #####adjust this
							name +='.xml'
							resfile._setroot(resroot)
							resfile.write(name)
							###cut to make if less files
							if g.tag!='nono':
								resroot.remove(g)

						if f.tag!='nono':
							resroot.remove(f)

					if e.tag!='nono':
						resroot.remove(e)

				if d.tag!='nono':
					resroot.remove(d)

			if c.tag!='nono':
				resroot.remove(c)
		
		if b.tag!='nono':
			resroot.remove(b)
