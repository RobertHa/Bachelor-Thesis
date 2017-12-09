import torch
from torch.autograd import Variable
from torch import nn, optim
import torch.nn.functional as F
import pickle
import sys
import math

from network import *
"""
class FFN(nn.Module):

	def __init__(self):
		super().__init__()
		self.h1 = torch.nn.Linear(2,2)
		self.h2 = torch.nn.Linear(2,5)
		self.h3 = torch.nn.Linear(5,1)

	def forward(self, x):
		x = self.h1(x)
		x = F.leaky_relu(x)
		x = self.h2(x)
		x = F.leaky_relu(x)
		x = self.h3(x)
		x = F.softmax(x)
		return x
"""

model = FFN()


torch.save(model, 'trained_model')
"""
with open('trained_model.pickle','wb') as save_model:
	pickle.dump(model.state_dict(), save_model,-1)
"""