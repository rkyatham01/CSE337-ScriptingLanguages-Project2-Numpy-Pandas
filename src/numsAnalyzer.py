# Run this script from the repository's root.
import numpy as np


def countMissingValues(x, k=0):
    if type(k) != type(5):
        raise ValueError("ValueError exception thrown")
    return (np.sum(np.isnan(x), axis=k))

def exams_with_median_gt_K(x, k):
    if type(k) != type(5):
        raise TypeError("Not the Same Type")

    if (k < 0) or (k > 100):
        raise ValueError("ValueError exception thrown")
    
    np.sort(x) #sort the rows nondecreasing order
    x[np.isnan(x)]= 0 #replacing the nans with 0

    for i in range(0, len(x)):
        for j in range(0, len(x[0])):
            if x[i][j] > 100 or x[i][j] < 0:
                raise ValueError("Greater than 100 or negative numbers in it")

    medArr = np.median(x, axis=1)
    c = 0
    for n in medArr:
        if n > k:
            c += 1
    return c

def curve_low_scoring_exams(x, k):
    if type(k) != type(5):
        raise TypeError("Not the Same Type")
        
    if (k < 0) or (k > 100):
        raise ValueError("ValueError exception thrown")

    x[np.isnan(x)]= 0 #replacing the nans with 0

    for i in range(0, len(x)):
        for j in range(0, len(x[0])):
            if x[i][j] > 100 or x[i][j] < 0:
                raise ValueError("Greater than 100 or negative numbers in it")

    avgArr = np.mean(x, axis=1)
    highestGrade = np.max(x,axis=1)

    for i in range(0, len(x)): #i is the respective semester
        if avgArr[i] < k: #average final score less than threshold, we curve
            curve = 100 - highestGrade[i]
            for j in range(0, len(x[0])):
                x[i][j] = x[i][j] + curve
    #now you argsort
    newArr = x[np.mean(x, axis=1).argsort()]
    return newArr



    
