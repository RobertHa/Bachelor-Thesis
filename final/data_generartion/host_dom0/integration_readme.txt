net = ANN('trained_model')
net.load_net(path) changes the model
net.schedulable(input_vector) returns True or False depending on the capabilities of the neural network
