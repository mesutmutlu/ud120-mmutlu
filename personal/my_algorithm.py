import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import  AdaBoostClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import  accuracy_score

classifiers = [KNeighborsClassifier(),
               AdaBoostClassifier(),
               RandomForestClassifier(),
               GaussianNB(),
               SVC(),
               DecisionTreeClassifier()]
names = ["KNeighborsClassifier",
         "AdaBoostClassifier",
         "RandomForestClassifier",
         "GaussianNB",
         "SVC",
         "DecisionTreeClassifier"]

for name, clf in zip(names, classifiers):

    print name + " started"
    clf = clf
    t0 = time()
    clf.fit(features_train, labels_train)
    print "training time:", round(time()-t0, 3), "s"
    t0 = time()
    pred = clf.predict(features_test)
    print "prediction time:", round(time()-t0, 3), "s"
    print "accuracy is" + str(accuracy_score(labels_test, pred))
