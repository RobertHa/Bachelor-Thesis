import torch
from network import FNN

class ANN:
	
	def __init__(self, path):
		self.model = torch.load(path)
		self.confidence = 0.0001

	def load_net(self,path):
		self.model = torch.load(path)

	def schedulable(self, in_vector):
		#convert input to Variable
		in_tensor = torch.autograd.Variable(torch.FloatTensor(in_vector))
		out = self.model(in_tensor)
		if (out.data[0] >= (1 - self.confidence)):#out.data[0] is necessary to access the value stored in the tensor variable
			return True
		return False
