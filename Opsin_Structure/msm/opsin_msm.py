import numpy as np
from msmbuilder.msm import ContinuousTimeMSM, MarkovStateModel
import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib.colors import LogNorm
import mdtraj.io as io
from matplotlib import gridspec
rcParams.update({'figure.autolayout': True})
rcParams['axes.linewidth'] = 3
rcParams.update({'font.size': 16})

assigns = []
for i in range(64):
    assigns.append(np.loadtxt('../assigns/assigns_%d.txt' %i ,dtype=int))
msm = MarkovStateModel(lag_time=500, n_timescales=20, reversible_type='transpose', ergodic_cutoff='off', prior_counts=0, sliding_window=True, verbose=True)
msm.fit(assigns)

try :
    ev0 = io.loadh('../tica_files/ev0.h5')['arr_0']
    ev1 = io.loadh('../tica_files/ev1.h5')['arr_0']
except:
    ev0, ev1 = [], []
    for i in range(64):
        a = io.loadh('on_tica_l16ns_%d.h5' %i)['arr_0'] 
        print a.shape
        ev0.extend(a[:,0])
        ev1.extend(a[:,1])

gens = np.loadtxt('../assigns/gens.txt')

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
    fig = plt.figure(figsize=(10,10),facecolor='w')
#    gs = gridspec.GridSpec(2,5)
    gs = gridspec.GridSpec(1,1)
    gs.update(left=0.1, right=0.95, bottom=0.05, top=0.95, wspace=0.0, hspace=0.05)
    for i in range(1,2):
        inner_grid = gridspec.GridSpecFromSubplotSpec(2, 1, subplot_spec=gs[i-1], wspace=0.0, hspace=0.0, width_ratios=[100,1,1], height_ratios=[1,1])
        ax = plt.Subplot(fig, inner_grid[0])
        www = ax.plot(msm.left_eigenvectors_[:,i],'.-',linewidth=2)#;ax.set_title('MSM eigenvector %d' %i,fontsize=16)
	if i != 0:
	    plt.text(30,0.03,'%3.2f (ns)' %(msm.timescales_[i-1]*80./1E3),\
                    color='k',fontsize=20,bbox=dict(facecolor='w', edgecolor='k',boxstyle='round'), horizontalalignment='center')
	    print i, '%3.2f (ns)' %(msm.timescales_[i-1]*80./1E3)
        ind1 = (msm.left_eigenvectors_[:,i] < 0)
        ind2 = (msm.left_eigenvectors_[:,i] > 0)
        sort1 = np.argsort(msm.left_eigenvectors_[:,i])
        fig.add_subplot(ax)
        ax = plt.subplot(inner_grid[1])
        ax.hist2d(ev0,ev1,bins=150,norm=LogNorm(),alpha=0.5)
        ms1 = [int(ii) for ii in abs(msm.left_eigenvectors_[:,i][ind1]/float(np.sum(abs(msm.left_eigenvectors_[:,i]))))*5000]
        ms2 = [int(ii) for ii in abs(msm.left_eigenvectors_[:,i][ind2]/float(np.sum(abs(msm.left_eigenvectors_[:,i]))))*5000]
	ax.scatter(gens[:,0][ind1],gens[:,1][ind1],s=ms1,c='r')
	ax.scatter(gens[:,0][ind2],gens[:,1][ind2],s=ms2,c='b')
#	ax.plot(gens[:,0][sort1[0:10]],gens[:,1][sort1[0:10]],'ro',markersize=10)
#	ax.plot(gens[:,0][sort1[-10:]],gens[:,1][sort1[-10:]],'bo',markersize=10)
#  	ax.xticks(fontsize=18)
#  	ax.yticks(fontsize=18)
#	plt.ylim([-0.05,0.05])
        fig.add_subplot(ax)
    plt.savefig('msm_relaxation_times3.pdf')
#    plt.show()

save()
plot_evs()
