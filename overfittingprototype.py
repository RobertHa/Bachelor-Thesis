import torch
from torch.autograd import Variable
from torch import nn, optim
import torch.nn.functional as F


test = 1000

batch_size = 13
dataset_size = batch_size*test
tasks_per_set = 10
params_per_task = 5
input_dimension = params_per_task*tasks_per_set
hidden_size = 3
num_classes = 2
learning_rate = 1




### making test values
testdata = []
for t in range(10):
	x = Variable(torch.randn(batch_size, input_dimension).type(torch.FloatTensor)).abs()
	#print(x)
	y = F.softmax(Variable(torch.randn(batch_size, num_classes).type(torch.FloatTensor)))
	#print(y)
	testdata.append((x,y))


class FFN(nn.Module):

	def __init__(self,input_size,hidden_size,num_classes):
		super().__init__()
		self.h1 = nn.Linear(input_size,hidden_size)
		self.h2 = nn.Linear(hidden_size,num_classes)

	def forward(self, x):
		x = self.h1(x)
		x = F.leaky_relu(x)
		x = self.h2(x)
		x = F.softmax(x)
		return x


model = FFN(input_size = input_dimension, hidden_size = hidden_size, num_classes = num_classes)
opt = optim.SGD(params = model.parameters(),lr = learning_rate)

for epoch in range(test-1):
	###load new batch
	x = testdata[epoch%2][0]
	y = testdata[epoch%2][1]
	out = model(x)
	loss = F.mse_loss(out,y)
	print(loss.data[0])
	model.zero_grad()
	loss.backward()
	opt.step()

#### after training we need the validation data:

test_x = testdata[1][0]
test_y = testdata[1][1]

out = model(test_x)
__,pred = out.max(1)
print('pred',pred.view(1,-1))
__,actual = test_y.max(1)
print('actual',actual.view(1,-1))

test_x = testdata[0][0]
test_y = testdata[0][1]

out = model(test_x)
__,pred = out.max(1)
print('pred',pred.view(1,-1))
__,actual = test_y.max(1)
print('actual',actual.view(1,-1))

print('und noch einer nicht aus dem trainings set:')

test_x = testdata[2][0]
test_y = testdata[2][1]

out = model(test_x)
__,pred = out.max(1)
print('pred',pred.view(1,-1))
__,actual = test_y.max(1)
print('actual',actual.view(1,-1))

print('OVERFITTING ACHIEVED!!!!!')