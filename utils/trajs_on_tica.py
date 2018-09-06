import numpy as np
import mdtraj.io as io
import mdtraj as md
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
from matplotlib import rcParams
rcParams.update({'figure.autolayout': True})
rcParams['axes.linewidth'] = 3
rcParams.update({'font.size': 20})
from tqdm import tqdm
import matplotlib.cm as cm

# load inputs for tICA landscape 
ev0 = io.loadh('ev0.h5')['arr_0']
ev1 = io.loadh('ev1.h5')['arr_0']

# plot each trajectory on tICA landscape 
# time moves from blue to red with dark blue representing beginning of trajectory and dark red end of trajectory. 

n_trajs = 3
plt.figure(figsize=(15,5))
ii = 1
for i in tqdm(range(n_trajs)):
    plt.subplot(1,3,ii)
    d = io.loadh('on_tica_l20_%s.h5'%i)['arr_0'][:,0:2]
    plt.hist2d(ev0,ev1,bins=300,norm=LogNorm(),alpha=0.6)
    # using strides to avoid plotting every frame
    for j in tqdm(range(d.shape[0]/100)):
        color = cm.jet(float(j)/(d.shape[0]/100),1)
        plt.plot(d[:,0][::100][j],d[:,1][::100][j],'o',color=color,markersize=8,alpha=0.8)
    plt.title(i)
    plt.xticks([])   
    plt.yticks([])   
    ii += 1

plt.savefig('trajs_on_tica.png')
plt.show()

