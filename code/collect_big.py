import sys
import os
import numpy as np
import math
from scipy.spatial import ConvexHull
from scipy.interpolate import UnivariateSpline
from shapely import wkt
from shapely import geometry

def collect_big_stele(big_x,big_y,big_A,stele_x,stele_y,stele_A,all_stele_x,all_stele_y,Kx,Ky,keep_meta,distp2):

	ecc_big=np.zeros((1,len(big_x)))
	for i in range(len(big_x)):
    	center, phi, axes = fit_ellipse(all_stele_x,all_stele_y)
    	if len(phi)!=0:
            ecc_big[i]=sqrt(pow(axes[1],2) - pow(axes[0],2))/axes[1]
    	elif i!=1:
            ecc_big[i]=mean(ecc_big[:(i-1)])
        else
            ecc_big[i]=0.5
    
	remove_inds=[]
	p=[]
    for i in range(len(Kx)):
        p.append(geometry.Point(Kx[i],Ky[i]))
    poly=geometry.Polygon(p)
	for i in range(1:len(big_x)):
    	D=np.zeros((1,len(big_x[i])))
    	for j in range(big_x[i]):
        	pt=geometry.Point(big_x[i][j], big_y[i][j])
            D[j]= poly.exterior.distance(pt)
    
   		corners = np.hstack(big_x[i],big_y[i])
        corners_sorted = PolygonSort(corners)
        area = PolygonArea(corners_sorted)
    	if ecc_big[i]>=0.9 && min(abs(D))<=distp2 and not (i in keep_meta) and area<5000  ########################todo
        	stele_x.append(big_x[i])
        	stele_y.append(big_y[i])
        	stele_A.append(area)
        	remove_inds.append(i)


	for i in range(len(remove_inds)):
        big_x.pop(remove_inds[i]-i)
        big_y.pop(remove_inds[i]-i)
        big_A.pop(remove_inds[i]-i)


	for i in range(len(remove_inds)):
    	for j in range(len(keep_meta)):
        	if keep_meta[j]>remove_inds[i]
            	keep_meta[j]=keep_meta[j]-1
      


	IN4=[]
	IN4_A=[]
	for i in range(len(big_x)):
    	IN2=[]
    	for j in range(len(big_x[i])):
        	if inpolygon(big_x{i}(j),big_y{i}(j),Kx,Ky)==1:   #########################################todo
            	IN2.append(j)
 
    	if len(IN2)==len(big_x[i]):
        	IN4.appned(i)
        	corners = np.hstack(big_x[IN4[-1]],big_y[IN4[-1]])
        	corners_sorted = PolygonSort(corners)
        	area = PolygonArea(corners_sorted)
        	IN4_A.append(area) 


	remove_inds=[]
	if len(IN4)!=0:
    	for i in range(len(IN4)):
        if len(np.setdiff(IN4(i),keep_meta))!=0
            stele_x.append(big_x[IN4[i]])
            stele_y.append(big_y[IN4[i]])
            stele_A.append(big_A[IN4[i]])
            remove_inds.append(IN4[i])

 	for i in range(len(remove_inds)):
        big_x.pop(remove_inds[i]-i)
        big_y.pop(remove_inds[i]-i)
        big_A.pop(remove_inds[i]-i)


	for i in range(len(remove_inds)):
    	for j in range(len(keep_meta)):
        	if keep_meta[j]>remove_inds[i]:
            	keep_meta[j]=keep_meta[j]-1

    return big_x,big_y,big_A,stele_x,stele_y,stele_A,all_stele_x,all_stele_y,ecc_big,keep_meta

