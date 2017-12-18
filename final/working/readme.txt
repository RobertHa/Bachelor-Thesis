This is the working directory.
The database was imported and the data was preprocessed,
before the prototype was trained.

The steps to use the scripts are:

-import the trainin_data.db (contianing the information about success/no success and the taskset parameters for each taskset).
-by executing createTrainingTable.py the table 'training' is created in the database

-by executing makeTensors.py the information in the 'training' table is preprocessed and cut into minibatches.
makeTensors.py takes three arguments: 
            - The ratio (float) of training data compared to the total available training data.
            - The minibatch size (int).
            - A 0 or 1 value for the renew flag, 0 representing False and 1 True.
The renew flag decides whether the data is shuffled anew or if an old batch is loaded from batch.pickle.
batch.pickle is created each time makeTensor.py is executed with the renew-flag set True.
The final output with the seperated trainain and validation sets is saved in data.pickle.

The prototype:
  The class, which describes our prototype model is defined in network.py.
  To import the network.py into other python programms the __init__.py file has to be in the same directory.
  The shallowprototype.py is executed taking four arguments:
            - The size of the first hidden layer.
            - The size of the second hidden layer.
            - The learning rate
            - The number of epochs, which should be performed.
  shallowprototype.py saves the trained model in trained_model and the dimensions of the model in pramameter.pickle.

The validation loads the trained_model and takes an argument (the confidence value (float) for the validation), 
  to perform the validation of the trained model with the validation data in data.pickle.
  
