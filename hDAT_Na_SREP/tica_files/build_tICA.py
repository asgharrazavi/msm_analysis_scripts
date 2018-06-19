import os,sys
import mdtraj.io as io
import msmbuilder.decomposition.tica as ti
import numpy as np


def train(start,stop,stride):
    dataset = []
    for i in range(50):
    	ref = np.loadtxt('%s/na2_na1_%d.txt' %(path,i))[start:stop:stride]
    	d = np.zeros((len(ref)-1,n_parms))
    	print "working on:", i
    	for p in range(n_parms):
	    data = np.loadtxt('%s/%s_%d.txt' %(path,parms[p],i))
	    try:
	        d[:,p][0:d.shape[0]] = data[:,1][start:start+d.shape[0]]
	    except:
	        d[:,p][0:d.shape[0]] = data[start:start+d.shape[0]]
    	dataset.append(d)
    return dataset

tica = ti.tICA(n_components=None, lag_time=10)

parms = ['r60_y335','r60_e446','r60_e428','na2_water_coord',  'na2_e428',  'na2_d421',  'na2_d79',  'e428_r445',  \
'y335_e428',  'd436_r445',  'r60_d436',  'na2_na1']
n_parms = len(parms)

path = '/Users/asr2031/Desktop/transfer/dDAT_WT_ensemble_carver/000_all_skip20/analysis/'
dataset1 = train(0,-1,1)
tica.fit(dataset1)
print tica.eigenvalues_
tica.save('tica_l16ns_jul21_2017_clipped.h5')


