import os,sys
import mdtraj.io as io
import msmbuilder as msm
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
import numpy as np
import mdtraj as md
from matplotlib import rcParams
rcParams.update({'figure.autolayout': True})
rcParams['axes.linewidth'] = 3

def project():
    dataset, ev0, ev1 = [], [], []
    for i in range(50):
  	print i
	try:
    	    ref = np.loadtxt('na2_na1_%d.txt' %i)[:,1]
	except:
    	    ref = np.loadtxt('na2_na1_%d.txt' %i)
    	d = np.zeros((len(ref)-1,n_parms))
    	for p in range(n_parms):
	    data = np.loadtxt('%s_%d.txt' %(parms[p],i))
	    try:
	    	d[:,p] = data[:,1]
	    except:
	    	d[:,p] = data
        proj = np.dot(d,tica['components'].T)
	ev0.extend(proj[:,0])
	ev1.extend(proj[:,1])
	io.saveh('on_tica_l16ns_%d.h5' %(i), proj)
    	dataset.append(proj)
    io.saveh('ev0.h5',np.array(ev0))
    io.saveh('ev1.h5',np.array(ev1))
    return dataset

parms = ['r60_y335','r60_e446','r60_e428','na2_water_coord',  'na2_e428',  'na2_d421',  'na2_d79',  'e428_r445',  \
'y335_e428',  'd436_r445',  'r60_d436',  'na2_na1']

n_parms = len(parms)

tica = io.loadh('tica_l16ns.h5')

project()
