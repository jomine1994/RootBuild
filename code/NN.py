import sys
import os
import scipy
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



def NN(close_x,close_y,close_A,NNd,detail,I,results_dir,filename):
 	mean_close=np.zeros((len(close_x),2))
	for i in range(len(close_x)):
    	mean_close[i][0]=mean(close_x[i])
    	mean_close[i][1]=mean(close_y[i])
		D_close=scipy.spatial.distance.pdist(mean_close,'euclidean')
		D2_close=scipy.spatial.distance.squareform(D_close)
		to_remove=[]
		for i in range(D2_close.shape[1]):
    		D2_close[:,i]=np.sort(D2_close[:,i])
    		if D2_close[6][i]>NNd:
        		to_remove.append(i)

	stele_x=close_x
	stele_y=close_y
	for i in range(len(to_remove)):
		stele_x.pop(to_remove[i]-i)
		stele_y.pop(to_remove[i]-i)

	stele_A=[]
	all_stele_x=[]
	all_stele_y=[]
	for i in range(len(stele_x)):
		corners = np.hstack(stele_x[i],stele_y[i])
        corners_sorted = PolygonSort(corners)
        area = PolygonArea(corners_sorted)
    	stele_A.append(area)
    	all_stele_x=np.vstact(all_stele_x,stele_x[i])    	
    	all_stele_y=np.vstact(all_stele_y,stele_y[i])


	center, phi, axes = fit_ellipse(all_stele_x,all_stele_y)
	theta_r  = np.linspace(0,2*pi);
    ellipse_x_r = center[0] + axes[0]*cos( theta_r );
    ellipse_y_r = center[1] + axes[1]*sin( theta_r );
    #rotated_ellipse = R * [ellipse_x_r;ellipse_y_r];
    coord=np.hstack(ellipse_x_r,ellipse_y_r)
    p=path.Path(coord)
    to_del=[]
	inds=[]
	IN=[]
	for i in range(len(close_x)):
    	for j in range(len(close_x[i])):
        	IN[i][j]=p.contains_points(close_x[i][j],close_y[i][j])
    if not False in In[i]:
        inds.append(i)

	stele_x=[]
	stele_y=[]
	stele_A=[]
	all_stele_x=[]
	all_stele_y=[]
	for i in range(len(inds)):
    	stele_x.append(close_x[inds[i]])
    	stele_y.append(close_y[inds[i]])
    	corners = np.hstack(close_x[inds[i]],close_y[inds[i]])
    	corners_sorted = PolygonSort(corners)
    	area = PolygonArea(corners_sorted)
    	stele_A.append(area)
    	all_stele_x=np.vstact(all_stele_x,stele_x[i])    	
    	all_stele_y=np.vstact(all_stele_y,stele_y[i])


	for i in range(len(to_remove)):
		close_x.pop(inds[i]-i)
		close_y.pop(inds[i]-i)
		close_A.pop(inds[i]-i)

 	return stele_A,ellip,stele_x,stele_y,all_stele_x,all_stele_y,close_x,close_y,close_A