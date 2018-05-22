import os,sys
import mdtraj.io as io
import msmbuilder.decomposition.tica as ti
import numpy as np

tica = ti.tICA(n_components=None, lag_time=20)

def train(start,stop,stride):
    dataset = []
    for i in range(4):
	data = io.loadh('../../../stage1/analysis/t%d.h5' %i)['distances']
    	print "working on:", i, data.shape
    	dataset.append(data)
    for i in range(20):
	data = io.loadh('../../../stage2/analysis/t%d.h5' %i)['distances']
    	print "working on:", i, data.shape
    	dataset.append(data)
    for i in range(20):
	data = io.loadh('../../../stage3/analysis/t%d.h5' %i)['distances']
    	print "working on:", i, data.shape
    	dataset.append(data)
    for i in range(20):
	data = io.loadh('../../../stage4/analysis/t%d.h5' %i)['distances']
    	print "working on:", i, data.shape
    	dataset.append(data)
    return dataset

dataset1 = train(0,-1,1)
tica.fit(dataset1)
print tica.eigenvalues_
tica.save('tica_l20.h5')


