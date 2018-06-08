import numpy as np
import msmbuilder.tpt as tpt
from msmbuilder.msm import ContinuousTimeMSM, MarkovStateModel
import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams.update({'figure.autolayout': True})

assigns = []
for i in range(64):
    assigns.append(np.loadtxt('macro12_assigns_%d.txt' %i ,dtype=int))
# 40 ns
msm = MarkovStateModel(lag_time=500, n_timescales=20, reversible_type='transpose', ergodic_cutoff='off', prior_counts=0, sliding_window=True, verbose=True)
msm.fit(assigns)

def do_tpt(ev_id):
    plt.figure(figsize=(15,10))
    sources = [7]
    sinks = [10]
#    sources = np.where(msm.left_eigenvectors_[:,ev_id] < -0.05)
#    sinks = np.where(msm.left_eigenvectors_[:,ev_id] > 0.05)
    net_flux = tpt.net_fluxes(sources, sinks, msm, for_committors=None)
    np.savetxt('net_flux.txt',net_flux)
    pfold = tpt.committors(sources, sinks, msm)
    np.savetxt('pfold.txt',pfold)
    paths = tpt.paths(sources, sinks, net_flux, remove_path='subtract', flux_cutoff=0.9999999999)
#    mfpts = tpt.mfpts(msm, sinks, lag_time=20.0)
    mfpts = tpt.mfpts(msm, sinks=None, lag_time=1.0)    #     Default is (1) which is in units of the lag time of the MSM.
    print "mfpts:", mfpts
    np.savetxt('mfpts_from_i_to_j.txt',np.array(mfpts))
    total_flux = np.sum(paths[1])
    print "total_flux:", total_flux
    sort = np.argsort(pfold)
    total_line_width = np.sum(paths[1][0:5])
    for j in range(5):
	print "path:", paths[0][j]
	print "flux:", paths[1][j] , paths[1][j] / float(np.sum(paths[1]))
	x = []
	for k in range(len(paths[0][j])):
	    x.extend(np.where(np.arange(100)[sort] == paths[0][j][k])[0])
	plt.plot(x,pfold[paths[0][j]],linewidth=np.log(paths[1][j]/float(total_line_width)))
    plt.legend(['%1.8f' %i for i in paths[1][0:5]],fontsize=18,loc='upper left')
    for i in range(len(pfold)):
       	plt.plot(i,pfold[sort[i]],'o')
       	plt.text(i,pfold[sort[i]],sort[i])
    plt.savefig('pfold_ev%d_0.01.png' %ev_id)


for i in [1]:
    print "working on eigenvector:", i
    do_tpt(i)
