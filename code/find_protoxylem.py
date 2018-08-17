import sys
import os
import scipy
import numpy as np
import math

def find_protoxylem(stele_x,stele_y,stele_A,Kx,Ky,big,Xc,Yc,distp):

	proto_inds=np.where(stele_A>big)
	to_remove=[]
	for i in range(len(Kx)):
        p.append(geometry.Point(Kx[i],Ky[i]))
    poly=geometry.Polygon(p)
	for i in range(len(proto_inds)):
    	d1=sqrt( pow((Xc-mean(stele_x[proto_inds[i]])),2) + pow((Yc-mean(stele_y[proto_inds[i]])),2) )
    	pt=geometry.Point(mean(stele_x[proto_inds[i]]), mean(stele_y[proto_inds[i]]))
        d2= poly.exterior.distance(pt)
    	d2=abs(d2);
    	if d1<d2 or d2<distp:
       		to_remove.append(i) 
    for i in range(len(to_remove)):
		proto_inds.pop(to_remove[i]-i)

	return proto_inds

