#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("C:\\Users\\dtmemutlu\\PycharmProjects\\ud120-projects\\tools")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###

features_train = features_train[:len(features_train)/100]
labels_train = labels_train[:len(labels_train)/100]

CL = [10000]#[10, 100, 1000, 10000]
for i in CL:
    from sklearn.svm import SVC
    clf = SVC(kernel="rbf", C=float(i))
    t0 = time()
    clf.fit(features_train, labels_train)
    print "SVC Linear training time with C"+str(i), round(time()-t0, 3), "s"

    t0 = time()
    pred = clf.predict(features_test)
    print "SVC Linear prediction time with C"+str(i), round(time()-t0, 3), "s"

    print(pred[10], pred[26], pred[50])

    from sklearn.metrics import accuracy_score

    print features_test[10]
    print features_test[26]
    print features_test[50]

    print labels_test[9]
    print labels_test[25]
    print labels_test[49]
    print len(pred)
    print type(pred)
    import numpy

    unique, counts = numpy.unique(pred, return_counts=True)
    print dict(zip(unique, counts))

    acc = accuracy_score(labels_test, pred)
    print acc

#########################################################


