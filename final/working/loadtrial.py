import torch
from torch.autograd import Variable
from torch import nn, optim
import torch.nn.functional as F
import pickle
import sys
import math


from network import *

model = torch.load('trained_model')

x = Variable(torch.randn(2))
print(x)
print(model(x))