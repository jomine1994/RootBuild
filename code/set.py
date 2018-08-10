import sys
import os



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

Results={};
Results{1,2}='Whole Root Area';
Results{1,3}='Whole Root Eccentricity';
Results{1,4}='Number of Cortex Cells';
Results{1,5}='Average Area of Cortex Cells';
Results{1,6}='Average Eccenctricity of Cortex Cells';
Results{1,7}='Stele Area';
Results{1,8}='Stele Eccentricity';
Results{1,9}='Number of Stele Cells';
Results{1,10}='Average Area of Stele Cells';
Results{1,11}='Average Eccentricity of Stele Cells';
Results{1,12}='Number of Metaxylem Cells';
Results{1,13}='Average Area of Metaxylem Cells';
Results{1,14}='Eccentricity of Metaxylem Cells';
Results{1,15}='Number of Endodermis Cells';
Results{1,16}='Average Area of Endodermis Cells';
Results{1,17}='Eccentricity of Endodermis Cells';
if spec==2
    Results{1,18}='Number of Protoxylem Cells';
    Results{1,19}='Average Area of Protoxylem Cells';
    Results{1,20}='Average Eccentricity of Protoxylem Cells';
    Results{1,21}='Number of Aerenchyma Cells';
    Results{1,22}='Average Area of Aerenchyma Cells';
    Results{1,23}='Average Eccentricity of Aerenchyma Cells';
end


