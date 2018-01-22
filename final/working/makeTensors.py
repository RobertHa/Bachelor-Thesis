import sqlite3
import pickle
import sys
import torch
import math
from random import shuffle
from torch.autograd import Variable



training_validation_ratio = float(sys.argv[1])
minibatch_size = int(sys.argv[2])
renew = (int(sys.argv[3]) == 1)

batch = []

if renew:
	db = sqlite3.connect('training_data.db').cursor()
	dataset = db.execute('SELECT * FROM training')

	for item in dataset:
		ap = []
		ap.append(item[0])
		ap.append(item[1])
		ap.append(item[2]/1000)
		ap.append(item[4])
		ap.append(item[5]/1000)
		ap.append(item[7])
		ap.append(item[8]/1000)
		ap.append(item[10])
		ap.append(item[11]/1000)
		ap.append(item[13])
		ap.append(item[14]/1000)
		ap.append(item[16])
		ap.append(item[17]/1000)
		ap.append(item[19])
		ap.append(item[20]/1000)
		ap.append(item[22])
		ap.append(item[23])
		
		batch.append(ap)


	shuffle(batch)

	with open('batch.pickle','wb') as b:
		pickle.dump(batch,b,-1)

else:
	# if not renewed load old batch
	with open('batch.pickle','rb') as f:
		batch = pickle.load(f)


####################################################################################
#UNTIL HERE PREPARING DATA, BELOW SPLITTING INTO TRAINING AND VALIDATION
####################################################################################

training_size = math.floor((len(batch)//minibatch_size)*training_validation_ratio)#in number of minibatches

training = []
counter = 0
for c in range(training_size):
	#uncomment if you want to see the structure of an entry
	#if counter == 0:
	#	print(batches[0])
	x = []
	y = []
	for i in range(minibatch_size):
		x.append(list(batch[counter][1:-2]))
		y.append(list(batch[counter][-2:-1]))
		counter = counter + 1
	training.append((Variable(torch.FloatTensor(x)),Variable(torch.FloatTensor(y))))


validate = []
for i in range(counter,len(batch)):
	validate.append((Variable(torch.FloatTensor(list(batch[i][1:-2]))),Variable(torch.FloatTensor(list(batch[i][-2:-1])))))


with open('data.pickle','wb') as d:
	pickle.dump([training,validate],d, -1)


print('length of all dataset:',len(batch))
print('size of trainingset in number of minibatches:',training_size)
print(len(validate),'entries for validation')
print('##############################################################')