import numpy as np
import matplotlib.pyplot as plt
import mdtraj.io as io
from matplotlib.colors import LogNorm
import matplotlib.cm as cm
from matplotlib import rcParams
rcParams['axes.linewidth'] = 3
rcParams.update({'font.size': 16})

map15 = np.loadtxt('map15_pccaplus.dat')
assigns = np.loadtxt('macro15_assigns.txt')
gens = np.loadtxt('../gens_all_skip20.txt')
ev0 = io.loadh('../../tica_files/ev0.h5')['arr_0']
ev1 = io.loadh('../../tica_files/ev1.h5')['arr_0']
projections = np.load('../../tica_files/projected_on_tica_16ns_sep_skip20.npy')

plt.hexbin(ev0, ev1, bins='log', mincnt=1, cmap="Greys")

for i in range(15):
    c = cm.Paired(i/15.,1)
    ind = [map15 == i]
    plt.plot(gens[:,0][ind],gens[:,1][ind],'o',c=c,alpha=0.5,linewidth=0)#colors[i])
plt.legend(range(15),ncol=8,labelspacing=0.2,numpoints=1,handletextpad=0.01,handlelength=1.5,columnspacing=0.2,shadow=True,fancybox=True,fontsize=16,bbox_to_anchor=(0.85,1.1))

for i in range(15):
    c = cm.Paired(i/15.,1)
    ev00, ev11 = [], []
    for j in range(50):
	dd = projections[j][0:len(assigns[j])]
    	ind = [assigns[j] == i]
	if i in [0,1,2,3,4,5,7,8,12]:
	    stride = 1
	else:
	    stride = 10
	ev00.extend(dd[:,0][ind][0:-1:stride])
	ev11.extend(dd[:,1][ind][0:-1:stride])
    plt.scatter(ev00,ev11,c=c,cmap='gist_ncar',alpha=0.8, linewidths=0.5)

plt.savefig('img_macrostates.png',dpi=100)

