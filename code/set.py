import sys
import os
from tqdm import tqdm
from skimage import io
from skimage.measure import label
from skimage.color import rgb2gray
import cv2
import PIL.Image
import numpy as np
sys.path.append('D:\\RootAnalyzer_source\\RootAnalyzer_source')
from seg_and_det import seg_and_det


def load_set(path):
	f = open(path,'r');
	lines=f.readlines()
	dname=lines[0].strip() #root directory storing all images
	W=int(lines[1].strip()) #window size
	Di=float(lines[2].strip()) #Difference for mean threshold 0.05
	big=float(lines[3].strip()) #big=1000; %Threshold for large cells 1x1000 0.5x300 2x3000
	small=float(lines[4].strip()) #Threshold for small cells 1x50 0.5x15 2x150
	NNd=float(lines[5].strip()) #Distance threshold for nearest neighbours algorithm
	distp=float(lines[6].strip()) #Distance of small not-stele cell to convex hull of stele
	distp2=float(lines[7].strip()) #Distance of big not-stele cell to convex hull of stele
	spec=float(lines[8].strip())
	detail=float(lines[9].strip())
	results_dir=lines[10].strip()
	
	#Get names of images. Remove any non-image files.
	imnames=[]
	files=os.listdir(dname)
	for file in files:
		imnames.append(file)

	Results=[];
	Results.append('Whole Root Area')
	Results.append('Whole Root Eccentricity')
	Results.append('Number of Cortex Cells')
	Results.append('Average Area of Cortex Cells')
	Results.append('Average Eccenctricity of Cortex Cells')
	Results.append('Stele Area')
	Results.append('Stele Eccentricity')
	Results.append('Number of Stele Cells')
	Results.append('Average Area of Stele Cells')
	Results.append('Average Eccentricity of Stele Cells')
	Results.append('Number of Metaxylem Cells')
	Results.append('Average Area of Metaxylem Cells')
	Results.append('Eccentricity of Metaxylem Cells')
	Results.append('Number of Endodermis Cells')
	Results.append('Average Area of Endodermis Cells')
	Results.append('Eccentricity of Endodermis Cells')
	if spec==2:
		Results.append('Number of Protoxylem Cells')
		Results.append('Average Area of Protoxylem Cells')
		Results.append('Average Eccentricity of Protoxylem Cells')
		Results.append('Number of Aerenchyma Cells')
		Results.append('Average Area of Aerenchyma Cells')
		Results.append('Average Eccentricity of Aerenchyma Cells')
	for file in tqdm(imnames):
			I=io.imread(dname+file,as_gray=True);
			filename=file.split('.')[0]
			coord,x,y,A,xb,yb,BW=seg_and_det(I,W,Di,small,results_dir,filename,detail)
			'''coord,x,y,A= remove_interior_cell(coord,x,y,A,I,BW)
			endo_x,endo_y,endo_A,x,y,A = add_epidermis(x,y,A,xb,yb)
			small_x,small_y,small_A,big_x,big_y,big_A,num_big,num_small=size_classify_cells(x,y,A,big,small)
    		center, phi, axes = fit_ellipse(big_x[0],big_y[0])
    		dists,X0,Y0,bs_x,bs_y,meanz2 = dist2cent(num_small,small_x,small_y,big_x,big_y)
    		num_close,close_x,close_y,close_A,all_close_x, all_close_y=find_near(dists,small_x,small_y)
    		stele_A,ellip,stele_x,stele_y,all_stele_x,all_stele_y,close_x,close_y,close_A = NN(close_x,close_y,close_A,NNd,detail,I,results_dir,filename)
   			meta,_,_=find_meta(num_big,big_x,big_y,ellip,stele_A)
    		if spec==1:
        		Xc,Yc,keep_meta= remove_meta2(meta,big_x,big_y,bs_x,meanz2,close_A)
    		elif spec==2:
        		Xc,Yc,keep_meta= remove_meta3(meta,big_x,big_y,bs_x,meanz2,close_A);
    		stele_x,stele_y,num_stele,stele_A,big_x,big_y,big_A=metaxylem_noise(meta,keep_meta,len(stele_x), stele_x,stele_y,big_x,big_y,big_A,stele_A,all_stele_x,all_stele_y)
    		Kx,Ky,last_ellip,all_stele_x,all_stele_y,stele_x,stele_y,stele_A,remove_inds,cent_stele,D_stele,close_ecc,close_x,close_y,close_A = collect_small_stele(all_stele_x,all_stele_y,numel(close_x),close_x,close_y,close_A,stele_x,stele_y,stele_A,Xc,Yc,distp)
    		big_x,big_y,big_A,stele_x,stele_y,stele_A,all_stele_x,all_stele_y,ecc_big,keep_meta = collect_big_stele(big_x,big_y,big_A,stele_x,stele_y,stele_A,all_stele_x,all_stele_y,Kx,Ky,keep_meta,distp2)
    		big_x,big_y,big_A,stele_x,stele_y,stele_A,num_stele,num_big,keep_meta,ecc_big,Kx,Ky,ecc,keep_meta_A,tr = remove_stele(stele_x,stele_y,stele_A,big_x,big_y,big_A,close_x,close_y,Kx,Ky,keep_meta,big)
			'''



load_set('set.txt')


