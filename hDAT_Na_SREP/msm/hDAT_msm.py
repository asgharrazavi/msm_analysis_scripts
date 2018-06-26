import numpy as np
from msmbuilder.msm import ContinuousTimeMSM, MarkovStateModel
import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams.update({'figure.autolayout': True})
rcParams['axes.linewidth'] = 3

assigns = np.loadtxt('assigns_all_skip20.txt' ,dtype=int)
msm = MarkovStateModel(lag_time=30, n_timescales=20, reversible_type='transpose', ergodic_cutoff='off', prior_counts=0, sliding_window=True, verbose=True)
msm.fit(assigns)

def save():
    np.savetxt('msm_eigenvalues.dat',msm.eigenvalues_)
    np.savetxt('msm_left_eigenvectors.dat',msm.left_eigenvectors_)
    np.savetxt('msm_populations.dat',msm.populations_)
    s = [[i,msm.mapping_[i]] for i in range(len(msm.mapping_))]
    np.savetxt('msm_mapping.dat',np.array(s),fmt='%d')
    np.savetxt('msm_timescales.dat',msm.timescales_)
    np.savetxt('msm_timescales_uncertainty.dat',msm.uncertainty_timescales())
    np.savetxt('msm_tmat.dat',msm.transmat_)
    np.savetxt('msm_cmat.dat',msm.countsmat_)


def plot_evs():
    plt.figure(figsize=(20,10))
    for i in range(1,10):
        plt.subplot(3,3,i);plt.plot(msm.left_eigenvectors_[:,i],'.-',linewidth=2);plt.title('MSM eigenvector %d' %i,fontsize=16)
	if i != 0:
	    plt.text(30,0.03,'%3.2f (ns)' %(msm.timescales_[i-1]*80*20./1E3),\
                    color='k',fontsize=20,bbox=dict(facecolor='w', edgecolor='k',boxstyle='round'), horizontalalignment='center')
  	plt.xticks(fontsize=18)
  	plt.yticks(fontsize=18)
	plt.ylim([-0.05,0.05])
    plt.savefig('img_msm_relaxation_times.png')

save()
plot_evs()
