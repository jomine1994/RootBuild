import sys
import os
import numpy as np
import math
from scipy.spatial import ConvexHull
from scipy.interpolate import UnivariateSpline
from shapely import wkt
from shapely import geometry



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



def collect_small_stele(all_stele_x,all_stele_y,close_x,close_y,close_A,stele_x,stele_y,stele_A,Xc,Yc,distp):
    points = np.hstack(all_stele_x,all_stele_y)
    hull = ConvexHull(points)
    Kx=[]
    Ky=[]
	for simplex in hull.simplices:
        Kx.append(all_stele_x[simplex])
        Ky.append(all_stele_x[simplex])
    f = UnivariateSpline(Kx, Ky, s=1)
    Kx = np.linspace(Kx.min(), Kx.max(), 1000)
    Ky = f(Kx)

    close_ecc=np.zeros((1,len(close_x)))
    
    p=[]
    for i in range(len(Kx)):
        p.append(geometry.Point(Kx[i],Ky[i]))
    poly=geometry.Polygon(p)

    remove_inds=[]
    for i in range(len(close_x)):
        for j in range(len(close_x[i]):
            pt=geometry.Point(close_x[i][j],close_y[i][j]))
            d= poly.exterior.distance(pt)
            if abs(d)<distp
                stele_x.append(close_x[i])
                stele_y.append(close_y[i])
                corners = np.hstack(close_x[i],close_y[i])
                corners_sorted = PolygonSort(corners)
                area = PolygonArea(corners_sorted)
                stele_A.append(area)
                remove_inds.append(i)
                break
    
        center, phi, axes = fit_ellipse(close_x[i],close_y[i])
    
        if len(phi)!=0:
            close_ecc[i]=sqrt(pow(axes[1],2) - pow(axes[0],2))/axes[1]
        elif i!=1:
            close_ecc[i]=mean(close_ecc[:(i-1)])
        else:
            close_ecc[i]=0.5

    for i in range(len(remove_inds)):
        close_x.pop(remove_inds[i]-i)
        close_y.pop(remove_inds[i]-i)
        close_A.pop(remove_inds[i]-i)

    num_stele=len(stele_x);
    cent_stele=np.zeros((num_stele,2))
    D_stele=np.zeros((1,num_stele))
    for i in range(num_stele):
        all_stele_x.append(stele_x[i])
        all_stele_y.append(stele_y[i])
        cent_stele[i][0]=sum(stele_x[i])/len(stele_x[i])
        cent_stele[i][1]=sum(stele_y[i])/len(stele_y[i])
        D_stele[i]=sqrt(pow((Xc-cent_stele[i][0]),2) + pow((Yc-cent_stele[i][1]),2))

    center, phi, axes = fit_ellipse(all_stele_x,all_stele_y)
    last_ellip=[]
    last_ellip.append(center)
    last_ellip.append(phi)
    last_ellip.append(axes)
    points = np.hstack(all_stele_x,all_stele_y)
    hull = ConvexHull(points)
    Kx=[]
    Ky=[]
    for simplex in hull.simplices:
        Kx.append(all_stele_x[simplex])
        Ky.append(all_stele_x[simplex])

    return Kx,Ky,last_ellip,all_stele_x,all_stele_y,stele_x,stele_y,stele_A,remove_inds,cent_stele,D_stele,close_ecc,close_x,close_y,close_A