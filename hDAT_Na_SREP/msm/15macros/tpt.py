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
    total_flux = np.sum(paths[1])
    data = []
    acuu_f = 0
    for j in range(len(paths[1])):
	acuu_f += paths[1][j]/float(total_flux)
	data.append([paths[0][j],paths[1][j],paths[1][j]/float(total_flux),acuu_f])
    print tabulate(data,headers=('Path','Flux','Norm Flux','Accumulated Flux'),floatfmt='1.4f')

do_tpt()
