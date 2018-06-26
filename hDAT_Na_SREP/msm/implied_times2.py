import numpy as np
import matplotlib.pyplot as plt
from msmbuilder.msm import ContinuousTimeMSM, MarkovStateModel
from msmbuilder.msm import implied_timescales
import matplotlib as mpl
mpl.rcParams['axes.linewidth'] = 1 #set the value globally

sequences = np.loadtxt('assigns_all_skip20.txt',dtype=int)

lag_times = [5,10,15,20,30,50,100]
lag_times = [5,10,15,20,30,50,100,200,300]
n_timescales = 10

def plot(data,title,outname):
    plt.figure()
    for i in range(n_timescales):
   	plt.plot(lag_times, data[:, i], 'o-')
    plt.title(title)
    plt.semilogy()
    plt.xticks([5,15,30,50,100],np.array([5,15,30,50,100])*20*80/1000,fontsize=18)
    plt.yticks(fontsize=18)
    plt.xlabel('Lag times (ns)',fontsize=22)
    plt.ylabel('Implied times (ns)',fontsize=22)
    plt.savefig(outname)
    plt.close()

msm_timescales_d = implied_timescales(sequences, lag_times, n_timescales=n_timescales, n_jobs=1,msm=MarkovStateModel(verbose=True,  reversible_type='transpose',ergodic_cutoff=0),verbose=1)
plot(msm_timescales_d,'Discrete-time MSM Relaxation Timescales','imp_test.png')
quit()

#msm_timescales_d_mle = implied_timescales(sequences, lag_times, n_timescales=n_timescales, n_jobs=1,msm=MarkovStateModel(verbose=True,  reversible_type='mle',ergodic_cutoff=1),verbose=1)
msm_timescales_d_mle = implied_timescales(sequences, lag_times, n_timescales=n_timescales, n_jobs=1,msm=MarkovStateModel(verbose=True),verbose=1)
plot(msm_timescales_d_mle,'Discrete-time MSM Relaxation Timescales MLE','imp_times_mle.png')

msm_timescales_c = implied_timescales(sequences, lag_times, n_timescales=n_timescales, n_jobs=1, msm=ContinuousTimeMSM(verbose=True),verbose=1)
plot(msm_timescales_c,'Continuous-time MSM Relaxation Timescales MLE','imp_times_c.png')

