#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []
    #print predictions

    #print type(predictions), type(ages), type(net_worths)
    import numpy as np
    #errors = net_worths-predictions
    features = np.concatenate((ages,net_worths, predictions, abs(net_worths-predictions)),axis=1)
    #print features.shape
    sorted_features =  np.sort(features.view('i8,i8,i8,i8'), order=['f3'], axis=0).view(np.float)
    #print sorted_features
    cleaned_data = np.delete(sorted_features,2,1)[:81]
    print cleaned_data.shape
    #cleaned_data= sorted_features[:81,:3]

    #print cleaned_data


    #print features

    ### your code goes here
#    for p, a, nw in predictions, ages, net_worths:
        #print p, a, nw


    
    return cleaned_data

