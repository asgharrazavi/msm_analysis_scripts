import numpy as np
import matplotlib.pyplot as plt
import mdtraj.io as io
from matplotlib import rcParams
rcParams.update({'figure.autolayout': True})
rcParams['axes.linewidth'] = 2
rcParams.update({'font.size': 20})

# load parameters for labeling
parms = np.loadtxt('parms.txt',dtype=str)
print len(parms)

# load tICA and extract tICA eigenvectors
ti = io.loadh('tica_l16ns.h5')
evs = ti['vecs']

# plot first three tICA eigenvectors
plt.figure(figsize=(30,7))

# dividing by total sum of eigenvectors for normalization. It is better to use vector norms.
plt.plot(evs[:,0]/float(np.sum(abs(evs[:,0]))),'-ro',linewidth=2)
plt.plot(evs[:,1]/float(np.sum(abs(evs[:,1]))),'-bo',linewidth=2)
plt.plot(evs[:,2]/float(np.sum(abs(evs[:,2]))),'-go',linewidth=2)
plt.plot([-0.5,len(parms)],[0,0],'k')

# labeling axes and fancy legend
plt.legend(('tIC 1','tIC 2','tIC 3'),fontsize=20,ncol=3,handletextpad=0.2,shadow=True,fancybox=True,columnspacing=1,labelspacing=0.1,loc='upper center')
plt.ylabel('Normalized Eigenvector')
plt.xlabel('tICA Parameters')

plt.xlim([-0.5,len(parms)+1])
plt.xticks(range(len(parms)),parms,rotation='vertical',fontsize=12)
plt.savefig('tICA_evs.png',dpi=100)

# plot eigenvalues as well 
plt.figure(figsize=(10,10))
plt.plot(ti['vals'],'o-')
plt.savefig('tICA_vals.png')

