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

load_set('set.txt')


