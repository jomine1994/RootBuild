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


def find_meta(num_big,big_x,big_y,ellip,stele_A):
	IN3=[]
	IN3_A=[]
	for i in range(num_big):
    	IN2=[]
    	for j in range(len(big_x[i])):
        	if True:   ########################################to do
            	IN2.append(j)
    
    	if len(IN2)==len(big_x[i]):
        	IN3.append(i)
        	corners = np.hstack(big_x[IN3[i]],big_y[IN3[i]])
        	corners_sorted = PolygonSort(corners)
        	area = PolygonArea(corners_sorted)
        	IN3_A.append(area)



	bothCells_A=stele_A
	Mcells=mean(bothCells_A)
	Scells=std(bothCells_A)
	meta=[]
	for i in range(len(IN3)):
    	if abs(IN3_A[i]-Mcells)>3*Scells:
        	meta.append(IN3[i])
 
	Xcc=[]
	Ycc=[]
	if len(meta)==1:
    	Xc=sum(big_x[meta])/len(big_x[meta])
    	Yc=sum(big_y[meta])/len(big_y[meta])
	else:
    	for i in range(len(meta)):
        	Xcc.append(big_x[meta[i]])
        	Ycc.append(big_y[meta[i]])
    	Xc=sum(Xcc)/len(Xcc)
    	Yc=sum(Ycc)/len(Ycc)

    return meta,Xc,Yc
