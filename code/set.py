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
			coord,x,y,A= remove_interior_cell(coord,x,y,A,I,BW)
			endo_x,endo_y,endo_A,x,y,A = add_epidermis(x,y,A,xb,yb)
			small_x,small_y,small_A,big_x,big_y,big_A,num_big,num_small=size_classify_cells(x,y,A,big,small)
    
    if detail==2
        figure
        imshow(I)
        hold on
        for i=1:numel(small_x)
            plot(small_x{i},small_y{i},'r','LineWidth',2)
        end
        saveas(gcf,[results_dir,filename,'\size.jpg'])
        close(gcf)
        drawnow; pause(0.05);
    end



load_set('set.txt')


