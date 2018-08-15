import sys
import os
from skimage import io
from skimage.filters import threshold_otsu, threshold_local
from skimage import measure,color
from skimage.measure import label
from skimage.morphology import dilation,disk
import scipy.signal as signal
from scipy.interpolate import interp1d
from scipy.interpolate import griddata
from scipy import interpolate
from scipy.ndimage import convolve
from scipy.ndimage.filters import gaussian_filter,maximum_filter
from scipy.ndimage.morphology import distance_transform_edt
import pandas as pd
import scipy
from PIL import Image
import numpy as np
import cv2
from pylab import *
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import path
from PIL import Image, ImageDraw
from skimage import draw
import numpy as np

def poly2mask(vertex_row_coords, vertex_col_coords, shape):
    fill_row_coords, fill_col_coords = draw.polygon(vertex_row_coords, vertex_col_coords, shape)
    mask = np.zeros(shape, dtype=np.bool)
    mask[fill_row_coords, fill_col_coords] = True
    return mask

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


def seg_and_det(I,W,Di,small,results_dir,filename,detail):
    ###################################### Get binary image
    width=I.shape[0]
    height=I.shape[1]
    IM=signal.medfilt(I,W)
    sIM=IM-I-Di*255
    BW=sIM
    for i in range(width):
        for j in range(height):
            if sIM[i][j]>0:
                BW[i][j]=1
            else:
                BW[i][j]=0
    if detail==2:
        io.imsave(results_dir+filename+"_seg.png",BW)
    

    ##################################### Get coordinates and area of connected components 
    conn,num=label(BW,connectivity=2,return_num=True)
    props=measure.regionprops(conn)
    listing=[]
    for i in range(num):
        if props[i].area<small:
            listing.append(props[i].coords)

    for i in range(len(listing)):
        for j in range(listing[i].shape[0]):
            x=listing[i][j][0]
            y=listing[i][j][1]
            BW[x][y]=0
    
    BW=dilation(BW,selem=np.ones((2,2)))
    contours=plt.contour(double(BW), levels=[0.0,0.0])
    lines = []
    for line in contours.collections[0].get_paths():
        lines.append(line.vertices)
    X=[]
    Y=[]
    A=[]
    coord=[]
    for i in range(len(lines)):
        corners = lines[i]
        corners_sorted = PolygonSort(corners)
        area = PolygonArea(corners_sorted)
        if area>=small:
            A.append(area)
            X.append(np.array(lines[i][:,0]))
            Y.append(np.array(lines[i][:,1]))
            coord.append(np.array(lines[i]))
    max_area=max(A)
    ind=A.index(max(A))
    p=path.Path(coord[ind])
    to_del=[]
    for i in range(len(A)):
       if False in p.contains_points(coord[i]):
            if i!=ind:
                to_del.append(i)
    for i in range(len(to_del)):
        X.pop(to_del[i]-i)
        Y.pop(to_del[i]-i)
        A.pop(to_del[i]-i)
        coord.pop(to_del[i]-i)

    ########################################### Gain approximation of entire root boundary
    ind=A.index(max(A))
    mask=poly2mask(X[ind],Y[ind], I.shape)
    for i in range(width):
        for j in range(height):
            if mask[i][j]:
                mask[i][j]=1
            else:
                mask[i][j]=0
    contours=plt.contour(double(mask), levels=[0.0,0.0])
    lines = []
    for line in contours.collections[0].get_paths():
        lines.append(line.vertices)

    A_b=[]
    X_b=[]
    Y_b=[]
    for i in range(len(lines)):
        corners = lines[i]
        corners_sorted = PolygonSort(corners)
        area = PolygonArea(corners_sorted)
        A_b.append(area)
        X_b.append(np.array(lines[i][:,0]))
        Y_b.append(np.array(lines[i][:,1]))
    max_area=max(A_b)
    ind=A_b.index(max(A_b))
    xb=X_b[ind]
    yb=Y_b[ind]
    print(xb)
    print(yb)

    ############################################ Add missed cortex cells
    '''BW_orig=BW
    D_orig=distance_transform_edt(BW_orig)
    BW=gaussian_filter(BW,3)
    D=distance_transform_edt(BW)
    regmax= maximum_filter(D,size=3)
    ii=np.where(regmax==1)[0]
    jj=np.where(regmax==1)[1]
    ij=np.where(regmax==1)
    print(ii.shape)
    ij=np.asarray(ij)
    ij=ij.transpose()
    IN=[]
    for i in range(len(coord)):
        P=path.Path(coord[i])
        re=p.contains_points(ij)
        IN.append(re)
    IN=np.asarray(IN)
    print(IN.shape)
    minpeakheight=15;
    to_remove=[];
    for i in range(len(ii)):
        if True in IN[:,i]:
            to_remove.append(i)
        elif ii[i]<=10 or ii[i]>=width-10 or jj[i]<=10 or jj[i]>=height-10:
            to_remove.append(i)
        elif D_orig[ii[i]][jj[i]]<minpeakheight:
            to_remove.append(i)
    ii=list(ii)
    jj=list(jj)
    ij=list(ij)
    for i in range(len(to_remove)):
        ii.pop(to_remove[i]-i)
        jj.pop(to_remove[i]-i)
        ij.pop(to_remove[i]-i)

    ############################################### Take a finer segmentation to find cell boundaries
    IM=signal.medfilt(I,W)
    sIM=IM-I-Di*255/2
    BW=sIM
    for i in range(width):
        for j in range(height):
            if sIM[i][j]>0:
                BW[i][j]=1
            else:
                BW[i][j]=0

    conn,num=label(BW,connectivity=2,return_num=True)
    props=measure.regionprops(conn)
    listing=[]
    for i in range(num):
        if props[i].area<small:
            temp=props[i].coords
            listing.append(temp)
    for i in range(len(listing)):
        for j in range(listing[i].shape[0]):
            x=listing[i][j][0]
            y=listing[i][j][1]
            BW[x][y]=0
    strel=disk(5)
    BW=dilation(BW,selem=strel)

    contours=plt.contour(double(BW), levels=[0.0,0.0])
    lines = []
    for line in contours.collections[0].get_paths():
        lines.append(line.vertices)
    X2=[]
    Y2=[]
    A2=[]
    coord2=[]
    for i in range(len(lines)):
        corners = lines[i]
        corners_sorted = PolygonSort(corners)
        area = PolygonArea(corners_sorted)
        if area>=small:
            A2.append(area)
            X2.append(np.array(lines[i][:,0]))
            Y2.append(np.array(lines[i][:,1]))
            coord2.append(np.array(lines[i]))
    max_area=max(A2)
    ind=A2.index(max(A2))
    A.pop(ind)
    X2.pop(ind)
    Y2.pop(ind)
    coord2.pop(ind)
    ii=np.asarray(ii)
    jj=np.asarray(jj)
    ij=np.asarray(ij)
    remove_ind=[]
    for i in range(len(X2)):
        P=path.Path(coord2[i])
        re=p.contains_points(ij)
        if False in re:
            remove_ind.append(i)
    for i in range(len(remove_ind)):
        A.pop(remove_ind[i]-i)
        X2.pop(remove_ind[i]-i)
        Y2.pop(remove_ind[i]-i)
        coord2.pop(remove_ind[i]-i)
    X_all=np.concatenate(X,X2)
    Y_all=np.concatenate(Y,Y2)
    coord_all=np.concatenate(coord,coord2)
    A_all=np.concatenate(A,A2)'''
    return coord,X,Y,A,xb,yb,BW






    #IM=convolve(I, W, mode='nearest')
    #BW=im2bw(sIM,0);
    #adaptive_thresh = threshold_local(I, W, offset=0)
    #print(adaptive_thresh)
    #im = BW > adaptive_thresh
    #im=BW-I-Di

    #ImageDraw.Draw(BW).polygon(coord[0], outline=1, fill=1)
    #mask = numpy.array(img)
    #plt.plot(mask)