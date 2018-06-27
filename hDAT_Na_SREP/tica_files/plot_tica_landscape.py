import mdtraj.io as io
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rcParams
rcParams.update({'figure.autolayout': True})
rcParams['axes.linewidth'] = 3
rcParams.update({'font.size': 20})
from matplotlib.colors import LogNorm 

# load MD on tICA projected files
data1 = np.load('projected_on_tica_16ns_sep.npy')
data2 = np.load('projected_on_tica_16ns_sep_skip20.npy')

# concatenate tIC 1 and tIC 2 data
ev0 = []
ev1 = []
for i in range(len(data1)): 
    ev0.extend(data1[i][:,0])
    ev0.extend(data2[i][:,0])
    ev1.extend(data1[i][:,1])
    ev1.extend(data2[i][:,1])

# plot tICA landscape
plt.hist2d(ev0,ev1,bins=[200,400],norm=LogNorm())
plt.grid(True,lw=1)
plt.xlim([np.min(ev0)-0.1,np.max(ev0)+0.5])
plt.xlabel('tIC 1')
plt.ylabel('tIC 2')
plt.savefig('img_tica_landscape',dpi=100,transparet=True)

