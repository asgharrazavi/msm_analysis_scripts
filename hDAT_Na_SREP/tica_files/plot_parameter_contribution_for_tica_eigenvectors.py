import numpy as np
import matplotlib.pyplot as plt
import mdtraj.io as io
from matplotlib import rcParams
rcParams.update({'figure.autolayout': True})
rcParams['axes.linewidth'] = 2
rcParams.update({'font.size': 20})


parms = ['R60-Y335','R60-E446','R60-E428','Na2 water Coord. Num.',  'Na2-E428',  'Na2-E421',  'Na2-D79',  'E428-R445',  \
'Y335-E428',  'D436-R445',  'R60-D436',  'Na2-Na1']

ti = io.loadh('tica_l16ns_new_pars12.h5')
evs = ti['vecs']
plt.figure(figsize=(10,7))
plt.plot(evs[:,0]/float(np.sum(abs(evs[:,0]))),'-ro',linewidth=2)
plt.plot(evs[:,1]/float(np.sum(abs(evs[:,1]))),'-bo',linewidth=2)
plt.plot([-0.5,12.5],[0,0],'k')
plt.legend(('tIC 1','tIC 2'),fontsize=20,ncol=3,handletextpad=0.2,shadow=True,fancybox=True,columnspacing=1,labelspacing=0.1,loc='upper center')
plt.ylabel('Normalized Eigenvector')
plt.xlabel('tICA Parameters')
plt.xlim([-0.5,11.5])

plt.xticks(range(12),parms,rotation='vertical')
plt.savefig('parameter_contribution_for_tica_eigenvectors.png',dpi=200)

