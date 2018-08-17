import sys
import os
import numpy as np
import math




def size_classify_cells(x,y,A,big,small):
	# Categorised as big, small, tiny based on area
	np_A=np.asarray(A)
	sorted_index=np.argsort(np_A)
	sorted_A=np.sort(np_A)
	num_big=len(sorted_A[np.where(A>big)])
	num_tiny=len(sorted_A[np.where(A<=small)])
	num_small=len(A)-num_big-num_tiny;

	big_x=[]
	big_y=[]
	big_A=[]
	for i in range(num_big):
    	big_x.append(x[sorted_index[num_tiny+num_small+i]])
    	big_y.append(y[sorted_index[num_tiny+num_small+i]])
    	big_A.append(A[sorted_index[num_tiny+num_small+i]])

	small_x=[]
	small_y=[]
	small_A=[]
	for i in range(num_small):
    	small_x.append(x[sorted_index[num_tiny+i]])
    	small_y.append(y[sorted_index[num_tiny+i]])
    	small_A.append(A[sorted_index[num_tiny+i]])

return small_x,small_y,small_A,big_x,big_y,big_A,num_big,num_small