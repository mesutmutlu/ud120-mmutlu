#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""
from __future__ import division
import sys
sys.path.append("C:\\Users\\dtmemutlu\\PycharmProjects\\ud120-projects\\tools")
from feature_format import featureFormat
import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

#print enron_data
print len(enron_data.keys())
print enron_data.keys()[1]
print len(enron_data.values()[1])


print enron_data.keys()

print enron_data["PRENTICE JAMES"]
print enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]
print enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]
print enron_data["FASTOW ANDREW S"]["total_payments"]
print enron_data["SKILLING JEFFREY K"]["total_payments"]
print enron_data["LAY KENNETH L"]["total_payments"]
print max(enron_data["FASTOW ANDREW S"]["total_payments"],enron_data["SKILLING JEFFREY K"]["total_payments"],
          enron_data["LAY KENNETH L"]["total_payments"])

j=0
k=0
m=0
n=0
h=0
for name, features in enron_data.items():
    if enron_data[name]["salary"] == "NaN":
        j= j+1

    if enron_data[name]["email_address"] == "NaN":
        k=k+1

    if enron_data[name]["total_payments"] == "NaN":
        m=m+1

    if enron_data[name]["poi"] == True:
        n=n+1

    if enron_data[name]["poi"] == True and enron_data[name]["total_payments"]=="NaN":
        h = h + 1


print "numpy"
enron_numpy = featureFormat(enron_data, ["salary"])
print len(enron_numpy)
#print enron_data

#print enron_data[""]["email_address"]

print "nan salary number is", j,len(enron_data), j/len(enron_data)
print "nan email number is", k
print "number of total paymetns nan", m, len(enron_data), m/len(enron_data)
print "numbe rof poi", n
print "numbe rof poi with total_payments nan", h

print 1/3

l_poi = []
i = 0
for name, features in enron_data.items():
    if enron_data[name]["poi"] == 1:
        i = i+1
        l_poi.append(name.split(" ")[0] + " " + name.split(" ")[1])
        #print name.split(" ")
        #print name[0,name.indexOf(" ", name.indexOf(" ") + 1)];




#print i

text_file = open("../final_project/poi_names.txt", "r")
lines = text_file.readlines()[2:]
#print type(lines)
for l in lines:
    #if l.startswith("(y)"):
    #print l[4:-1].replace(",", "").upper()
    #print l[3:-1].split(",")[0][1:], l[3:-1].split(",")[1][1:]
    l_poi.append(l[4:-1].replace(",", "").upper())
text_file.close()
#print l_poi



def unique(list1):
    # intilize a null list
    unique_list = []

    # traverse for all elements
    for x in list1:
        # check if exists in unique_list or not
        if x not in unique_list:
            unique_list.append(x)
            # print list
    return unique_list

#print len(unique(l_poi))
