import torch
from torch.autograd import Variable
from torch import nn, optim
import torch.nn.functional as F
import pickle
import sys
import math
from network import FFN

tasks_per_set = 7
params_per_task = 2
input_dimension = params_per_task*tasks_per_set
num_classes = 1	

hidden_size_1 = int(sys.argv[1])
hidden_size_2 = int(sys.argv[2])
learning_rate = float(sys.argv[3])


with open('data.pickle','rb') as p:
	data = pickle.load(p)
training = data[0]


model = FFN(input_size = input_dimension, hidden_size_1 = hidden_size_1, hidden_size_2 = hidden_size_2, num_classes = num_classes)
opt = optim.Adam(params = model.parameters(),lr = learning_rate)

lr_factor = 10

for epoch in range(int(sys.argv[4])):
	if epoch%100 == 0:
		learning_rate = learning_rate/100
		opt = optim.Adam(params = model.parameters(),lr = learning_rate)
	
	for minibatch in range(len(training)):
		x = training[minibatch][0]
		y = training[minibatch][1]
		out = model(x)
		loss = F.mse_loss(out,y)
		if epoch%10 == 0 and minibatch%50 ==0:
			print(epoch, 'epoch |err: ',loss.data[0])
		model.zero_grad()
		loss.backward()
		opt.step()


torch.save(model, 'trained_model')

with open('parameter.pickle','wb') as parameter_save:
	pickle.dump([input_dimension,hidden_size_1,hidden_size_2],parameter_save, -1)


print(len(training),'minibatches ran\n################################################################################')
