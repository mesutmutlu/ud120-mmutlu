#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""
#from __future__ import division
import pickle
import sys
sys.path.append("C:\\Users\\dtmemutlu\\PycharmProjects\\ud120-projects\\tools")

from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### your code goes here
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import  accuracy_score
clf = DecisionTreeClassifier()
clf.fit(features, labels)
pred = clf.predict(features)
print accuracy_score(labels, pred)

from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.3, random_state=42)
clf2 = DecisionTreeClassifier()
clf2.fit(X_train, y_train)
pred2 = clf2.predict(X_test)
print accuracy_score(y_test, pred2)
print len(pred2)
print pred2
print 25/29
import numpy as np
print np.asarray(y_test)
from sklearn.metrics import precision_score, recall_score

print precision_score(np.asarray(y_test), pred2)
print recall_score(np.asarray(y_test), pred2)
print type(pred2), type(np.asarray(y_test))

