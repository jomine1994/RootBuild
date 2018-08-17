import sys
import os
import numpy as np
import math


def metaxylem_noise(meta,keep_meta,num_stele,stele_x,stele_y,big_x,big_y,big_A,stele_A,all_stele_x,all_stele_y):
	S=numpy.setdiff1d(meta,keep_meta)
	if len(S)!=0:
    	for i in range(len(S)):
        	stele_x.append(big_x[S[i]])
        	stele_y.append(big_y[S[i]])
        	stele_A.append(big_A[S[i]])
    	for i in range(len(S)):
    		big_x.pop(S[i]-i)
    		big_y.pop(S[i]-i)
    		big_A.pop(S[i]-i)

	num_stele=len(stele_x);
	IN5=[]
	for i in range(len(keep_meta)):
		p=path.Path(np.hstack(big_x[meta[i]],big_y[meta[i]]))
    	for j in range(num_stele):
        	IN2=[]
        	for k in range(len(stele_x[j])):
            	if p.contains_points(np.stack(stele_x[j][k],stele_y[j][k]))==True:
                	IN2.append(k)
        	if len(IN2)==len(stele_x[j]):
            	IN5.append(j)

	if len(IN5)!=0:
		for i in range(len(IN5)):
    		stele_x.pop(IN5[i]-i)
    		stele_y.pop(IN5[i]-i)
    		stele_A.pop(IN5[i]-i)

	num_stele=len(stele_x);
	return stele_x,stele_y,num_stele,stele_A,big_x,big_y,big_A