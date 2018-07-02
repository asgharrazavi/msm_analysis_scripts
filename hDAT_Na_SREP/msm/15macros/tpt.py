import numpy as np
import msmbuilder.tpt as tpt
from msmbuilder.msm import ContinuousTimeMSM, MarkovStateModel
import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams.update({'figure.autolayout': True})
from tabulate import tabulate

assigns = np.loadtxt('macro15_assigns.txt' ,dtype=int)
msm = MarkovStateModel(lag_time=30, n_timescales=20, reversible_type='transpose', ergodic_cutoff='off', prior_counts=0, sliding_window=True, verbose=True)
msm.fit(assigns)

def do_tpt():
    plt.figure(figsize=(15,10))
    # all trajectories start from macrostate 14
    sources = [14]
    # Na+/Na2 is released to intracellular environment at macrostates 5,7,2,3,1,0
    sinks = [5,7,2,3,1,0]
    net_flux = tpt.net_fluxes(sources, sinks, msm, for_committors=None)
    pfold = tpt.committors(sources, sinks, msm)
    paths = tpt.paths(sources, sinks, net_flux, remove_path='subtract', flux_cutoff=0.9999999999)
    sort = np.argsort(pfold)
    total_line_width = np.sum(paths[1][0:5])
    print tabulate([paths[0],paths[1]],headers=('Path','Flux'))
    for j in range(10):
	print "path:", paths[0][j]
	print "flux:", paths[1][j]

do_tpt()
