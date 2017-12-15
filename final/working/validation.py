import torch
from torch.autograd import Variable
from torch import nn, optim
import torch.nn.functional as F
import pickle
import sys
import math
from network import *

confidence = float(sys.argv[1])

model = torch.load('trained_model')

with open('data.pickle','rb') as p:
	data = pickle.load(p)
validate = data[1]

print('###############################VALIDATE#######################################')

val_size = len(validate)
success = 0
suc_sets = 0
pos_suc_sets = 0
suc_set_flag = False
for i in validate:
	x = i[0]
	if (i[1].data[0]==1):
		suc_set_flag = True
		suc_sets = suc_sets + 1
	y = i[1]
	out = model(x)
	
	if abs(y.data[0]-out.data[0])<=confidence:
		if suc_set_flag:
			pos_suc_sets = pos_suc_sets +1
			suc_set_flag = False
		success = success +1
print(success,'/',val_size, '|', (success/val_size))
print('working: right on', pos_suc_sets, 'out of', suc_sets, 'which is a quota of', (pos_suc_sets/suc_sets))
print('failing: right on', (success - pos_suc_sets), 'out of', (len(validate)-suc_sets), 'which is a quota of', ((success - pos_suc_sets)/(len(validate)-suc_sets)))