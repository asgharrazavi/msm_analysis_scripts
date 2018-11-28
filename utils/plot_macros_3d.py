import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import mdtraj.io as io
from matplotlib.colors import LogNorm
import itertools
colors = [''.join(a) for a in itertools.product(['o', 'd', '<', '>', '^', '*'],['r', 'b', 'g', 'c', 'm', 'k', 'y'])]
import matplotlib.cm as cm
from matplotlib import rcParams
#rcParams.update({'figure.autolayout': True})
rcParams['axes.linewidth'] = 3
rcParams.update({'font.size': 16})

map15 = np.loadtxt('map10_pccaplus.dat')
gens = np.loadtxt('gens.txt')
ev0 = io.loadh('ev0.h5')['arr_0']
ev1 = io.loadh('ev1.h5')['arr_0']
ev2 = io.loadh('ev2.h5')['arr_0']

tableau20 = ['r','b','g','gold','c','m','k','linen','silver','chocolate']

fig = plt.figure(figsize=(15,10))
ax = fig.add_subplot(111, projection='3d')
n_macros = int(np.max(map15) + 1)

if 0:
 for i in range(n_macros):
    c = cm.Paired(i/float(n_macros),1)
    ind = [map15 == i]
    ax.scatter(gens[:,0][ind], gens[:,1][ind], gens[:,2][ind], c=tableau20[i] ,marker='.')
 plt.legend(range(n_macros),ncol=8,labelspacing=0.2,numpoints=1,handletextpad=0.01,handlelength=1.5,columnspacing=0.2,shadow=True,fancybox=True,fontsize=16,bbox_to_anchor=(0.85,1.1))

def plot(n_trajs,name,start):
    for j in range(n_trajs):
	print j+start
    	m_assigns = np.loadtxt('macro10_assigns_%d.txt' %(j+start),dtype=int)
    	on_tica = io.loadh('../on_tica_l20_%s_%d.h5' %(name,j))['arr_0']
    	for i in range(15):
    	    c = cm.Paired(i/15.,1)
	    if i not in m_assigns: continue
	    ind = (m_assigns == i)
	    if i in [8,9]: 
	        ev0 = on_tica[ind][:,0]#[::200]	
	        ev1 = on_tica[ind][:,1]#[::200]	
	        ev2 = on_tica[ind][:,2]#[::200]	
	    elif i in [0,5]: 
	        ev0 = on_tica[ind][:,0]#[::100]	
	        ev1 = on_tica[ind][:,1]#[::100]	
	        ev2 = on_tica[ind][:,2]#[::100]	
	    else: 
	        ev0 = on_tica[ind][:,0]#[::10]
	        ev1 = on_tica[ind][:,1]#[::10]
	        ev2 = on_tica[ind][:,2]#[::10]
	    ax.scatter(ev0,ev1,ev2, c=tableau20[i] ,marker='o',alpha=0.2)

plot(4,'s1',0)
plot(20,'s2',4)
plot(20,'s3',24)
plot(20,'s4',44)
ax.set_xlabel('tIC 1')
ax.set_ylabel('tIC 2')
ax.set_zlabel('tIC 3')

#plt.savefig('land_macro_10_3d_2.png')
# rotate the axes and update
for angle in range(0, 360):
    ax.view_init(30, angle)
    plt.draw()
    plt.savefig('land_macro_10_3d_angle_%03d.png' %angle)
    plt.pause(.001)

#plt.show()

