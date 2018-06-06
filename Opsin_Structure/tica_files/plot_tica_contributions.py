import mdtraj.io as io
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rcParams
rcParams.update({'figure.autolayout': True})
rcParams['axes.linewidth'] = 3
rcParams.update({'font.size': 20})
 
# load tICA object
ti = io.loadh('tica_l20.h5')

vecs = ti['components']
cov = ti['covariance']

# calculate total dynamics
dott = np.dot(cov,vecs.T)
trr = 0
for i in range(dott.shape[0]):
    s = np.linalg.norm(dott[:,i])**2
    trr += s

# calculate each eigenvector's contribution
c3 = 0
cont = []
for i in range(dott.shape[0]):
    s = np.linalg.norm(dott[:,i])**2
    c3 += s / float(trr)
    cont.append(c3)

# plot accumulated tICA eigenvector contributions
plt.plot(cont,'o-',lw=2)
plt.xlim([-1,22])	# zooming only on the first 22 tICs
plt.ylim([0,1])
plt.grid(True,lw=1)
plt.xlabel('tICA eigenvector')
plt.ylabel('Contribution')
plt.savefig('tic_cont_zoom.png',dpi=100,transparet=True)
plt.show()

