
from __future__ import  division
import math


#print 1-3*0.918/4


#entrophy = -2/3 * (math.log(float(2/3),2)) - 1/3 * (math.log(float(1/3),2))
#print entrophy


def featureScaling(arr):
    x = (arr[1]-arr[0])/(arr[2]-arr[0])
    return x

# tests of your feature scaler--line below is input data
data = [115, 140, 175]
print featureScaling(data)
