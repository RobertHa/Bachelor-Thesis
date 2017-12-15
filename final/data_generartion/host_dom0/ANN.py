import torch
from network import FNN

class ANN:
	
	def __init__(self, path):
		self.model = torch.load(path)

	def load_net(self,path):
		"""loads a new model from the provided path"""
		self.model = torch.load(path)

	def schedulable(self, in_vector, confidence):
		"""evaluates the in_vector, returns 1 for schedulable, 0 for not 
		schedulable and the exact prediction if confidence can not be met"""
		in_tensor = torch.autograd.Variable(torch.FloatTensor(in_vector))#convert input to Variable
		out = self.model(in_tensor)
		if (out.data[0] >= (1 - confidence)):#out.data[0] to access the value stored in the tensor variable
			return True
		elif(out.data[0] <= confidence):
			return False
		else:
			return out.data[0]