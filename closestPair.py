import math


def distance(a,b):
    return math.sqrt((a[0]-b[0])*(a[0]-b[0]) + (a[1]-b[1])*(a[1]-b[1]))

def bruteForceMin(points):
    min = points[0]
    for i in range(0,len(points)):
        for j in range(i+1,len(points)):
            if(distance(points[i],points[j]<min)):
                min = distance(points[i],points[j])


    
    return min

def projectY(points):
    Y = []
    for i in range(0,len(points)):
        Y[i] = points[i][1]

    return Y

def projectX(points):
    X= []
    for i in range(0,len(points)):
        X[i] = points[i][0]

    return X