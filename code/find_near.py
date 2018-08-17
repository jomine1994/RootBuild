import sys
import os
import scipy
import numpy as np
import math
from sklearn.mixture import GaussianMixture


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
def find_near(dists,small_x,small_y):
	np_dists=np.asarray(dists)
	sorted_index=np.argsort(np_dists)
	sorted_dists=np.sort(np_dists)
	gmm = GaussianMixture(n_components=2, covariance_type='spherical')
	gmm.fit(dists)
	w=maxgmm.weights_
	max_index=w.index(max(w))
	close_thresh=gmm.means[max_index]+3*sqrt(gmm.covariances_[max_index])
	num_close=len(np_dists[np.where(dists<close_thresh)])
	close_x=[]
	close_y=[]
	close_A=[]
	all_close_x=[]
	all_close_y=[]
	for i in range(num_close):
    	close_x.append(small_x[sorted_index[i]])
    	close_y.append(small_y[sorted_index[i]])
    	corners = np.hstack(small_x[sorted_index[i]],small_y[sorted_index[i]])
        corners_sorted = PolygonSort(corners)
        area = PolygonArea(corners_sorted)
    	close_A.append(area)
    	all_close_x=np.vstact(all_close_x,close_x[i])    	
    	all_close_y=np.vstact(all_close_y,close_y[i])

    return num_close,close_x,close_y,close_A,all_close_x,all_close_y

