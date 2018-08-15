import sys
import os
import numpy as np
import math

def add_epidermis(x,y,A,xb,yb):
	len_cell=len(x)
	len_b=len(xb)
	mx=np.ones(len_cell)
	my=np.ones(len_cell)
	for i in range(len_cell):
    	mx[i]=mean(x[i])
    	my[i]=mean(y[i])

	endo=np.zeros(len_b)
	for i in range(len_b):
		t1=math.pow(xb[i]*np.ones(len_cell)-mx,2)
		t2=math.pow(yb(i)*np.ones(len_cell)-my,2)
    	d=math.sqrt(t1+t2)
    	dd=min(d)
    	endo[i]=dd

	endo=np.unique(endo)
	endo_thresh = np.percentile(A[endo],80)

	to_remove=[]
	endo_x=[]
	endo_y=[]
	endo_A=[]
	for i in range(len(endo)):
    	if A[endo[i]]<endo_thresh:
        	to_remove.append(i)
        	endo_x.append(x[endo[i]])
        	endo_y.append(y[endo[i]])
        	endo_A.append(A[endo[i]])
    for i in range(len(to_remove)):
    	x.pop(to_remove[i]-i)
    	y.pop(to_remove[i]-i)
    	A.pop(to_remove[i]-i)
	return endo_x,endo_y,endo_A,x,y,A