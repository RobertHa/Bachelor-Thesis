.db file has to be in directory
order of execution
1. createTrainingTable.py // creates table in db
2. makeTensors.py // creates batch.pickle if renew is activated and always data.pickle //3 args: (float training_validation_ratio) (int minibatch_size) (1/0 renew)
3. shallowprototype.py // loads data.pickle and creates a trained_model // 3 args: (int hidden_size1) (int hidden_size2) (float learning_rate)
4. validation.py // loads the trained_model // 1 arg: (float confidence)


