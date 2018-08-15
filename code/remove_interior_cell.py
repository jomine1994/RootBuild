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


def remove_interior_cell(coord,x,y,A,I,BW):
    to_remove=[]
    found_in=[]
    rem_rem=[]
    for i in range(1:len(x)):
        for j in range(1：len(x)):
            p=path.Path(coord[j])
            points=mean(coord[i])
               if not (False in p.contains_points(points)) and i!=j:
                   corners1 = coord[i]
                corners_sorted1 = PolygonSort(corners1)
                area1 = PolygonArea(corners_sorted1)
                corners2 = coord[j]
                corners_sorted2 = PolygonSort(corners2)
                area2 = PolygonArea(corners_sorted2)
                if area1<area2:
                    to_remove.append(i)
                    found_in.append(j)
                    rem_rem.append(j)
                else:
                    to_remove.append(j)
                    found_in.append(i)
                    rem_rem.append(i)

    for i in range(len(to_remove)):
        X.pop(to_del[i]-i)
        Y.pop(to_del[i]-i)
        A.pop(to_del[i]-i)
        coord.pop(to_del[i]-i)
    return coord,X,Y,A

