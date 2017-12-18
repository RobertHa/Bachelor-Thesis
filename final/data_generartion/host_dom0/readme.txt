The task descriptions for each task in the directories task1 to task7 were imported to host_dom0.

With the execution of createSets.py, the tasksets were created as combinations of the tasks and saved in a folder named 'sets'.
  The information about the taskset parameters was saved in data.pickle.
  For the execution of createSets.py resroot.xml needs to be in the same directory as a template for an xml file.

The dom0_p0.py worked on the tasksets in sets and wrote the logfiles into a directory named 'log'.

After all tasksets were processed, logToDB.py and writeTasksetsToDB.py created the database with tables 
  for the taskset parameters and the sucess or failure of each taskset.

To integrate a trained model into the dom0_p0.py:
  - the ANN.py and 
  - a network.py, definfing the structure of the model (see also in final/working/)
  - a trained_model to be integrated
 

As an explenation how to use the ANN container mudule in the dom0_p0.py:
  from ANN import *
  
  net = ANN('trained_model')
  net.load_net(path) changes the model
  net.schedulable(input_vector, confidence) returns True or False depending on the capabilities of the neural network,
    if confidence can not be met, the actual result of the model is returned
