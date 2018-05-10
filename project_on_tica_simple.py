import os,sys
import mdtraj.io as io
import msmbuilder as msm
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
import numpy as np
import mdtraj as md
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
from matplotlib import rcParams
rcParams.update({'figure.autolayout': True})
rcParams['axes.linewidth'] = 3
rcParams.update({'font.size': 20})

def project():
    dataset = []
    for i in range(50):
	ref1 = io.loadh('%s/traj%d_cc.h5' %(traj_path,i), name=parms[0])
    	d = np.zeros((len(ref1),n_parms))
    	print "working on:", i
    	for p in range(len(parms)):
	    data = io.loadh('%s/traj%d_cc.h5' %(traj_path,i), name=parms[p])
	    d[:,p] = data
        proj = np.dot(d,tica['components'].T)
	io.saveh('on_tica_l16ns_%d.h5' %(i), proj)
        dataset.append(proj)
    return dataset


parms_file = "params.txt"
traj_path = "../trajs/"

parms = np.loadtxt('%s' %parms_file,dtype=str)
tica = io.loadh('tica_l16ns.h5')

proj_data = project()

ev0, ev1, ev2 = [], [], []
for i in range(50):
    ev0.extend(proj_data[i][:,0]); ev1.extend(proj_data[i][:,1]); ev2.extend(t6[i][:,2])
ev0, ev1, ev2 = np.array(ev0), np.array(ev1), np.array(ev2)
io.saveh('ev0.h5',ev0)
io.saveh('ev1.h5',ev1)
io.saveh('ev2.h5',ev2)
print ev0.shape, ev1.shape, ev2.shape
x1,x2,y1,y2,z1,z2 = -5,2,-4,5,-4,3
plt.figure(figsize=(6,15))
plt.subplot(311)
plt.hist2d(ev0,ev1,bins=350,norm=LogNorm())#;plt.xlim([x1,x2]);plt.ylim([y1,y2])
plt.subplot(312)
plt.hist2d(ev0,ev2,bins=350,norm=LogNorm())#;plt.xlim([x1,x2]);plt.ylim([z1,z2])
plt.subplot(313)
plt.hist2d(ev1,ev2,bins=350,norm=LogNorm())#;plt.xlim([y1,y2]);plt.ylim([z1,z2])
plt.savefig('lands_tica.png')

