import numpy as np
import matplotlib.pyplot as plt
import mdtraj.io as io
from matplotlib.colors import LogNorm
import itertools
colors = [''.join(a) for a in itertools.product(['o', 'd', '<', '>', '^', '*'],['r', 'b', 'g', 'c', 'm', 'k', 'y'])]
import matplotlib.cm as cm
from matplotlib import rcParams
#rcParams.update({'figure.autolayout': True})
rcParams['axes.linewidth'] = 3
rcParams.update({'font.size': 16})

map15 = np.loadtxt('map15_pccaplus.dat')
assigns = np.loadtxt('macro_assigns_map15_pccaplus.txt')
gens = np.loadtxt('../gens_all_skip20.txt')
ev0 = io.loadh('../../ev0.h5')['arr_0']
ev1 = io.loadh('../../ev1.h5')['arr_0']

#plt.hist2d(ev0,ev1,bins=(500,200),cmap='Greys',norm=LogNorm(),alpha=0.5)
plt.hexbin(ev0, ev1, bins='log', mincnt=1, cmap="Greys")

for i in range(15):
#    c = cm.gist_ncar(i/15.,1)
    c = cm.Paired(i/15.,1)
    ind = [map15 == i]
#    plt.plot(gens[:,0][ind],gens[:,1][ind],colors[i])
    plt.plot(gens[:,0][ind],gens[:,1][ind],'o',c=c,alpha=0.5,linewidth=0)#colors[i])
plt.legend(range(15),ncol=8,labelspacing=0.2,numpoints=1,handletextpad=0.01,handlelength=1.5,columnspacing=0.2,shadow=True,fancybox=True,fontsize=16,bbox_to_anchor=(0.85,1.1))


for i in range(15):
#    c = cm.jet(i/15.,1)
    c = cm.Paired(i/15.,1)
    ev00, ev11 = [], []
    for j in range(50):
	dd = io.loadh('../../h5/on_tica_l16ns_all_skip20_%d.h5' %j)['arr_0']
    	ind = [assigns[j] == i]
	if i in [0,1,2,3,4,5,7,8,12]:
	    stride = 1
	else:
	    stride = 10
	ev00.extend(dd[:,0][ind][0:-1:stride])
	ev11.extend(dd[:,1][ind][0:-1:stride])
    print len(ev00)
    if i == 8:
        #plt.scatter(ev00,ev11,c='b',cmap='gist_ncar',alpha=0.8, linewidths=0.5)#colors[i])
        plt.scatter(ev00,ev11,c=c,cmap='gist_ncar',alpha=0.8, linewidths=0.5)#colors[i])
    else:
        plt.scatter(ev00,ev11,c=c,cmap='gist_ncar',alpha=0.8, linewidths=0.5)#colors[i])

plt.savefig('macros10_4.png',dpi=800)
#plt.show()

