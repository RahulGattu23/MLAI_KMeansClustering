# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 10:37:05 2021

@author: rahul
"""

## K-MEANS CLUSTERING

import numpy as np

x = ([2, 3, 4, 10, 11, 12, 20, 25, 30, 37, 43, 55, 56, 59, 63, 64, 65, 77, 86, 87])
k = 2

s1 = []
s2 = []

np.random.seed(200)

#Calculating distance
def c_dist(x, c1, c2):
    dist1 = np.absolute(x-c1)
    dist2 = np.absolute(x-c2)
    
    return dist1, dist2


def my_cluster(x, d1, d2):
    for i in range(len(x)):
        if d1[i] <=  d2[i]:
            s1.append(x[i])
        
        else:
            s2.append(x[i])
            
    print("s1 = {} ; s2 = {}".format(s1, s2))
    return s1, s2

#centroids
c1=x[np.random.randint(0,len(x))] #initial value of centroid1
c2=x[np.random.randint(0,len(x))] #initial value of centroid2
c1_old=c2_old=0
j=1

#clustering
while(~(c1_old == c1)):
    print("iteration:{}".format(j))
    d1,d2=c_dist(x,c1,c2)
    print("c1={}, c2={}".format(c1,c2))
    s1,s2=my_cluster(x,d1,d2)
    c1_old=c1
    c2_old=c2
    c1=np.mean(s1)
    c2=np.mean(s2)
    s1.clear()
    s2.clear()
    j=j+1

print("clustering completed")
