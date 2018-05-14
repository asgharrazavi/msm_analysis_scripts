import os,sys
import mdtraj.io as io
import msmbuilder.decomposition.tica as ti
import numpy as np

def train():
    dataset = []
    for i in range(50):
	ref1 = io.loadh('%s/traj%d_cc.h5' %(traj_path,i), name=parms[0])
    	d = np.zeros((len(ref1),n_parms))
    	print "working on:", i
    	for p in range(len(parms)):
	    data = io.loadh('%s/traj%d_cc.h5' %(traj_path,i), name=parms[p])
	    d[:,p] = data
    	dataset.append(d)
    return dataset


parms_file = "params.txt"
traj_path = "../trajs/"

parms = np.loadtxt('%s' %parms_file,dtype=str)

dataset = train()
np.save('dataset.npy',dataset)

tica = ti.tICA(n_components=None, lag_time=20)
tica.fit(dataset)

print "tICA eigenvalues: ", tica.eigenvalues_
tica.save('tica_l16ns.h5')


