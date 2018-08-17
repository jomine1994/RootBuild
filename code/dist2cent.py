import sys
import os
import scipy
import numpy as np
import math

def(num_small,small_x,small_y,big_x,big_y):
	meanz=np.zeros((num_small,2))
	for i in range(num_small):
    	meanz[i][0]=np.mean(small_x[i]) 
    	meanz[i][1]=np.mean(small_y[i]);
	X0=np.mean(meanz[:,0])
	Y0=np.mean(meanz[:,1])

	bs_x=np.vstack((big_x,small_x))
	bs_y=np.vstack((big_y,small_y))
	meanz2=np.zeros(len(bs_x),2)
	meanz2[0]=np.array([0,0])
	for i in range(1:len(bs_x)):
    	meanz2[i]=np.array([np.mean(bs_x[i]),np.mean(bs_y[i])])

	dists=np.zeros((1,num_small))
	for i in range(num_small):
    	dists[i]=math.sqrt(math.pow((small_x[i][0]-X0),2) + math.pow((small_y[i][1]-Y0),2))
    return dists,X0,Y0,bs_x,bs_y,meanz2
