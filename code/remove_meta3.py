import sys
import os
import numpy as np
import math


def PolygonSort(corners):
    n = len(corners)
    cx = float(sum(x for x, y in corners)) / n
    cy = float(sum(y for x, y in corners)) / n
    cornersWithAngles = []
    for x, y in corners:
        an = (np.arctan2(y - cy, x - cx) + 2.0 * np.pi) % (2.0 * np.pi)
        cornersWithAngles.append((x, y, an))
    cornersWithAngles.sort(key = lambda tup: tup[2])
    temp=map(lambda xyan: (xyan[0],xyan[1]), cornersWithAngles)
    return temp

def PolygonArea(corners):
    corners=list(corners)
    n = len(corners)
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += corners[i][0] * corners[j][1]
        area -= corners[j][0] * corners[i][1]
    area = abs(area) / 2.0
    return area



def remove_meta2(meta,big_x,big_y,bs_x,meanz2,close_A):
	keep_meta=[]
	if len(meta)!=1:
    	for i in range(len(meta)):
        	for j in range(len(big_x[meta[i]])):
            	curr_meta_x=big_x[meta[i]][j]*np.ones((len(bs_x),1))
            	curr_meta_y=big_y[meta[i]][j]*np.ones((len(bs_x),1))
            	D=sqrt(pow((curr_meta_x-meanz2[:,1]),2) + pow((curr_meta_y-meanz2[:,2]),2))
            	loc=D.indix(min(D))
            if not (loc in meta) and loc<=len(big_x):
                break
            if j==len(big_x[meta[i]]):
                keep_meta.append(meta[i])
      
	else:
    	keep_meta=meta


	MA=[]
	for i in range(len(keep_meta)):
		corners = np.hstack(big_x[keep_meta[i]],big_y[keep_meta[i]])
        corners_sorted = PolygonSort(corners)
        area = PolygonArea(corners_sorted)
		MA.append(area)

	Mcells=mean(np.hstack(close_A,MA))
	Scells=mean(np.hstack(close_A,MA))
	to_del=[]
	for i in range(len(keep_meta)):
    	if abs(MA[i]-Mcells)>2*Scells:
    	else
        	to_del.append(i)
    for i in range(len(to_del)):
		keep_meta.pop(to_del[i]-i)

	Xcc=[]
	Ycc=[]
	if len(keep_meta)==1:
    	Xc=sum(big_x[keep_meta])/len(big_x[keep_meta])
    	Yc=sum(big_y[keep_meta])/len(big_y[keep_meta])
	else:
    	for i in range(len(keep_meta)):
        	Xcc.append(big_x[keep_meta[i]])
        	Ycc.append(big_y[keep_meta[i]])
    	Xc=sum(Xcc)/len(Xcc)
    	Yc=sum(Ycc)/len(Ycc)

    return Xc,Yc,keep_meta


