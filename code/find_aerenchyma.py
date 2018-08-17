import sys
import os
import scipy
import numpy as np
import math

def find_aerenchyma(big_x,big_y,Kx,Ky):

	cortex_x=[]
	cortex_y=[]
	cortex_A=[]
	inds=[]
	for i in range(len(big_x)):
    	if ~inpolygon(mean(big_x{i}),mean(big_y{i}),Kx,Ky): ###################################################ToDo
        	cortex_x.append(big_x[i])
        	cortex_y.append(big_y[i])
        	cortex_A.append(area)
        	inds.append(i)

OF=gmdistribution.fit(cortex_A(2:end)',2);
[~,which_peak]=max(OF.mu);
aer_thresh=OF.mu(which_peak)-sqrt(OF.Sigma(which_peak));


% m=mean(cortex_A);
% s=std(cortex_A);
aeren_inds=[];
for i=1:numel(cortex_x)
    if cortex_A(i)>aer_thresh
       aeren_inds=[aeren_inds inds(i)];
    end
 end

