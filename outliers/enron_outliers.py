#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("C:\\Users\\dtmemutlu\\PycharmProjects\\ud120-projects\\tools")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
data_dict.pop( "TOTAL", 0 )
features = ["salary", "bonus"]
data = featureFormat(data_dict, features)
import numpy as np
sorted_data = np.sort(data.view('i8,i8'), order=['f1'], axis=0).view(np.float)
print sorted_data[len(sorted_data)-1:]

for key, values in data_dict.iteritems():
    if values["salary"] >= 1000000 and values["bonus"] >= 5000000 and values["bonus"] != "NaN" and values["salary"] != "NaN" :
        print key, values["salary"], values["bonus"]

for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()


### your code below



