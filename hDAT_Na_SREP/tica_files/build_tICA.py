import msmbuilder.decomposition.tica as ti
import numpy as np

def train():
    dataset = []
    for i in range(50):
    	ref = np.loadtxt('na2_na1_%d.txt' %(i))
    	d = np.zeros((len(ref)-1,n_parms))
    	print "working on:", i
    	for p in range(n_parms):
	    data = np.loadtxt('%s_%d.txt' %(parms[p],i))
	    try:
	        d[:,p] = data[:,1]	# some input files may have two columns, we always need the data (2nd column) not time (1st column)
	    except:
	        d[:,p] = data
    	dataset.append(d)
    return dataset

tica = ti.tICA(n_components=None, lag_time=10, gamma=0.05, weighted_transform=False)

parms = ['r60_y335','r60_e446','r60_e428','na2_water_coord',  'na2_e428',  'na2_d421',  'na2_d79',  'e428_r445',  \
'y335_e428',  'd436_r445',  'r60_d436',  'na2_na1']

n_parms = len(parms)

dataset = train()
tica.fit(dataset)

print "tica eigenvalues:", tica.eigenvalues_
tica.save('tica_l16ns.h5')


