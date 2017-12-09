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


#########################################
"""

class FFN(nn.Module):

	def __init__(self,input_size,hidden_size_1, hidden_size_2, num_classes):
		super().__init__()
		self.h1 = nn.Linear(input_size,hidden_size_1)
		self.h2 = nn.Linear(hidden_size_1, hidden_size_2)
		self.h3 = nn.Linear(hidden_size_2,num_classes)

	def forward(self, x):
		x = self.h1(x)
		x = F.leaky_relu(x)
		x = self.h2(x)
		x = F.leaky_relu(x)
		x = self.h3(x)
		x = F.sigmoid(x)
		return x
"""

#########################################

model = FFN(input_size = input_dimension, hidden_size_1 = hidden_size_1, hidden_size_2 = hidden_size_2, num_classes = num_classes)
opt = optim.Adam(params = model.parameters(),lr = learning_rate)


for epoch in range(len(training)):
	###load new batch
	x = training[epoch][0]
	y = training[epoch][1]
	out = model(x)
	loss = F.mse_loss(out,y)
	print('error of',loss.data[0])
	model.zero_grad()
	loss.backward()
	opt.step()


torch.save(model, 'trained_model')

with open('parameter.pickle','wb') as parameter_save:
	pickle.dump([input_dimension,hidden_size_1,hidden_size_2],parameter_save, -1)


print(len(training),'minibatches ran\n################################################################################')
