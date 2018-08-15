import sys
import os
import numpy as np
import math




def size_classify_cells(x,y,A,big,small):
	# Categorised as big, small, tiny based on area
[~,jj]=sort(A,'descend');
num_big=numel(A(A>big)); %1000
num_tiny=numel(A(A<=small)); %50?
% num_big=numel(new_A(new_A>200)); %1000
% num_tiny=numel(new_A(new_A<=10)); %50?
num_small=numel(x)-num_big-num_tiny;

% big_x, big_y, big_A are the biggest cells
big_x=cell(1,num_big);
big_y=cell(1,num_big);
big_A=zeros(1,num_big);
for i=1:num_big
    big_x{i}=x{jj(i)};
    big_y{i}=y{jj(i)};
    big_A(i)=polyarea(x{jj(i)},y{jj(i)});
end

% small_x, small_y, small_A are small cells, mostly in the stele
small_x=cell(1,num_small);
small_y=cell(1,num_small);
small_A=zeros(1,num_small);
for i=(num_big+1):(numel(x)-num_tiny)
    small_x{i-num_big}=x{jj(i)};
    small_y{i-num_big}=y{jj(i)};
    small_A(i)=polyarea(x{jj(i)},y{jj(i)});
end

return small_x,small_y,small_A,big_x,big_y,big_A,num_big,num_small