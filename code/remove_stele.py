import sys
import os
import scipy
import numpy as np
import math
import numpy.linalg as linal




def remove_stele(new_stele_x,new_stele_y,new_stele_A,big_x,big_y,big_A,close_x,close_y,Kx,Ky,meta2,big):


    all_new_stele_x=[]
    all_new_stele_y=[];
    for i in range(len(new_stele_x)):
        all_new_stele_x.append(new_stele_x[i])
        all_new_stele_y.append(new_stele_y[i])
        all_new_stele_ind.append(i*np.ones((1,len(new_stele_x[i]))))


    all_big_x=[]
    all_big_y=[]
    all_big_inds=[]
    for i in range(len(big_x)):
        all_big_x.append(big_x[i])
        all_big_y.append(big_y[i])
        all_big_inds.append(i*np.ones((1,len(big_x[i]))))

    remove_stele=[]
    for i in range(len(new_stele_x)):
        close_big=[]
        close_stele=[]
    
        AAA=np.where(all_new_stele_inds==i)
        t_all_new_stele_inds=all_new_stele_inds
        t_all_new_stele_inds[AAA]=[]
        t_all_new_stele_x=all_new_stele_x
        t_all_new_stele_x[AAA]=[]
        t_all_new_stele_y=all_new_stele_y
        t_all_new_stele_y[AAA]=[]
    
        for j in range(len(new_stele_x[i])):
        
            test_stele_x=new_stele_x[i][j]*np.ones((1,len(t_all_new_stele_inds)))
            test_stele_y=new_stele_y[i][j]*np.ones((1,len(t_all_new_stele_inds)))
            [ii,jj]=min( sqrt(pow((test_stele_x-t_all_new_stele_x),2) + pow((test_stele_y-t_all_new_stele_y),2)) )
        
            test_big_x=new_stele_x[i][j]*np.ones((1,len(all_big_inds)))
            test_big_y=new_stele_y[i][j]*np.ones((1,len(all_big_inds)))
            [kk,ll]=min( sqrt(pow((test_big_x-t_all_new_big_x),2) + pow((test_big_y-t_all_big_stele_y),2)) )
        
        if kk<ii:
            close_big.append(all_big_inds[ll])
        else:
            close_stele.append(t_all_new_stele_inds[jj])
    
        if len(np.unique(close_big))>len(np.unique(close_stele)):
            remove_stele.append(i)
            big_x.append(new_stele_x[i])
            big_y.append(new_stele_y[i])
            big_A.append(new_stele_A[i])

        for i in range(len(remove_stele)):
            new_stele_x.pop(remove_stele[i]-i)
            new_stele_y.pop(remove_stele[i]-i)
            new_stele_A.pop(remove_stele[i]-i)


    ecc=np.zeros((1,len(new_stele_x)))
    for i in range(len(new_stele_x)):
        center, phi, axes = fit_ellipse(new_stele_x[i],new_stele_y[i])
        if len(phi)!=0:
            new_stele_ecc[i]=0.5
        else:
            new_stele_ecc[i]=sqrt(pow(axes[1],2) - pow(axes[0],2))/axes[1]
            
    

    tr=[]
    for i in range(len(Kx)):
        p.append(geometry.Point(Kx[i],Ky[i]))
    poly=geometry.Polygon(p)
    for i in range(1:len((new_stele_x)):
        D=np.zeros((1,len((new_stele_x[i])))
        for j in range((new_stele_x[i]):
            pt=geometry.Point((new_stele_x[i][j], (new_stele_y[i][j])
            D[j]= poly.exterior.distance(pt)
    
        if new_stele_A(i)>big/2&min(abs(D))<1&&ecc(i)<0.5
        tr=[tr i];
        big_x=[big_x new_stele_x{i}];
        big_y=[big_y new_stele_y{i}];
        big_A=[big_A new_stele_A(i)];
    end
end
new_stele_x(tr)=[];
new_stele_y(tr)=[];
new_stele_A(tr)=[];



ecc_big=zeros(1,numel(big_x));
%roundness_big=zeros(1,numel(big_x));
for i=1:numel(big_x)
    [ellipse_aa,refit_aa] = fit_ellipse(big_x{i},big_y{i});
    
    if ~isempty(refit_aa)
        ecc_big(i)=sqrt(ellipse_aa.long_axis^2 - ellipse_aa.short_axis^2)/ellipse_aa.long_axis;
    elseif i~=1
        ecc_big(i)=mean(ecc_big(1:(i-1)));
    else
        ecc_big(i)=0.1;
    end
    
    %ecc_big(i)=sqrt(ellipse_aa.long_axis^2 - ellipse_aa.short_axis^2)/ellipse_aa.long_axis;
    %roundness_big(i)=ellipse_aa.short_axis/ellipse_aa.long_axis;
end

all_new_stele_x=[];
all_new_stele_y=[];
all_new_stele_inds=[];
for i=1:numel(new_stele_x)
    all_new_stele_x=[all_new_stele_x new_stele_x{i}'];
    all_new_stele_y=[all_new_stele_y new_stele_y{i}'];
    all_new_stele_inds=[all_new_stele_inds i*ones(1,numel(new_stele_x{i}))];
end

K=convhull(all_new_stele_x,all_new_stele_y);
Kx=all_new_stele_x(K);
Ky=all_new_stele_y(K);

num_stele=numel(new_stele_x);
num_big=numel(big_x);
ecc=zeros(1,num_stele);
roundness=zeros(1,num_stele);
% Record eccentricity of all cells in the stele
for i=1:num_stele
    [ellipse_aa,refit_aa] = fit_ellipse(new_stele_x{i},new_stele_y{i});
    if isempty(ellipse_aa.long_axis)
        ecc(i)=0.5;
    else
        ecc(i)=sqrt(ellipse_aa.long_axis^2 - ellipse_aa.short_axis^2)/ellipse_aa.long_axis;
    end
    %roundness(i)=ellipse_aa.short_axis/ellipse_aa.long_axis;
end

keep_meta_A=zeros(1,numel(meta2));
for i=1:numel(meta2)
    keep_meta_A(i)=big_A(meta2(i));
end

return big_x,big_y,big_A,new_stele_x,new_stele_y,new_stele_A,num_stele,num_big,meta2,ecc_big,Kx,Ky,ecc,keep_meta_A,tr