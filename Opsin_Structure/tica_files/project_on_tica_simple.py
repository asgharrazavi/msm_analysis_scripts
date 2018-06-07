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


def project(start,stop,stride):
    dataset = []
    for i in range(4):
	d = io.loadh('../../../stage1/analysis/t%d.h5' %i)['distances']
    	print "working on:", i, d.shape
        proj = np.dot(d,tica['components'].T)
	io.saveh('on_tica_l20_s1_%d.h5' %(i), proj)
        dataset.append(proj)
    for i in range(20):
	d = io.loadh('../../../stage2/analysis/t%d.h5' %i)['distances']
    	print "working on:", i, d.shape
        proj = np.dot(d,tica['components'].T)
	io.saveh('on_tica_l20_s2_%d.h5' %(i), proj)
        dataset.append(proj)
    for i in range(20):
	d = io.loadh('../../../stage3/analysis/t%d.h5' %i)['distances']
    	print "working on:", i, d.shape
        proj = np.dot(d,tica['components'].T)
	io.saveh('on_tica_l20_s3_%d.h5' %(i), proj)
        dataset.append(proj)
    for i in range(20):
	d = io.loadh('../../../stage4/analysis/t%d.h5' %i)['distances']
    	print "working on:", i, d.shape
        proj = np.dot(d,tica['components'].T)
	io.saveh('on_tica_l20_s4_%d.h5' %(i), proj)
        dataset.append(proj)
    return dataset

tica = io.loadh('tica_l20.h5')

t6 = project(0,-1,1)

ev0, ev1, ev2 = [], [], []
for i in range(64):
    ev0.extend(t6[i][:,0]); ev1.extend(t6[i][:,1]); ev2.extend(t6[i][:,2])
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

