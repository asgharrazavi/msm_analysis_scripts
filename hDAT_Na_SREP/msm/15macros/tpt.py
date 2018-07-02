import numpy as np
import msmbuilder.tpt as tpt
from msmbuilder.msm import ContinuousTimeMSM, MarkovStateModel
import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams.update({'figure.autolayout': True})

assigns = np.loadtxt('macro15_assigns.txt' ,dtype=int)
msm = MarkovStateModel(lag_time=30, n_timescales=20, reversible_type='transpose', ergodic_cutoff='off', prior_counts=0, sliding_window=True, verbose=True)
msm.fit(assigns)

def do_tpt(ev_id):
    plt.figure(figsize=(15,10))
    sources = [14]
    sinks = [5,7,2,3,1,0]
    net_flux = tpt.net_fluxes(sources, sinks, msm, for_committors=None)
    pfold = tpt.committors(sources, sinks, msm)
    paths = tpt.paths(sources, sinks, net_flux, remove_path='subtract', flux_cutoff=0.9999999999)
    sort = np.argsort(pfold)
    total_line_width = np.sum(paths[1][0:5])
    for j in range(5):
	print "path:", paths[0][j]
	print "flux:", paths[1][j]
	x = []
	for k in range(len(paths[0][j])):
	    x.extend(np.where(np.arange(100)[sort] == paths[0][j][k])[0])
	plt.plot(x,pfold[paths[0][j]],linewidth=np.log(paths[1][j]/float(total_line_width)))
    plt.legend(['%1.8f' %i for i in paths[1][0:5]],fontsize=18,loc='upper left')

for i in [1,8]:
    print "working on eigenvector:", i
    do_tpt(i)
