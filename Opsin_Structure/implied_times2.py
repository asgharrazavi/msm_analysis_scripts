import numpy as np
import matplotlib.pyplot as plt
from msmbuilder.msm import ContinuousTimeMSM, MarkovStateModel
from msmbuilder.msm import implied_timescales
import matplotlib as mpl
mpl.rcParams['axes.linewidth'] = 1 #set the value globally

sequences = []
for i in range(64):
    sequences.append(np.loadtxt('assigns_%d.txt' %i,dtype=int))

print len(sequences)
lag_times = [50,100,150,200,300,500,1000,2000]#,3000,4000,5000]
n_timescales = 7

def implied_times():
    i_times = np.zeros((len(lag_times),20))
    for i in range(len(lag_times)):
	msm = MarkovStateModel(lag_time=lag_times[i], n_timescales=20, reversible_type='transpose', ergodic_cutoff='off', prior_counts=0, sliding_window=True, verbose=True)
        msm.fit(sequences)
 	i_times[i] = msm.eigenvalues_[1:]
 	print i, msm.eigenvalues_

#implied_times()
#quit()


def plot(data,title,outname):
    plt.figure()
    for i in range(n_timescales):
   	plt.plot(lag_times, data[:, i], 'o-')
    plt.title(title)
    plt.semilogy()
#    plt.xticks([5,15,30,50,100],np.array([5,15,30,50,100])*20*80/1000,fontsize=18)
#    plt.xticks(lag_times,np.array(lag_times)*20*80/1000,fontsize=18)
#    plt.yticks([10,100,1000],np.array([10,100,1000])*20*80/1000,fontsize=18)
    plt.yticks(fontsize=18)
    plt.xlabel('Lag times ',fontsize=22)
    plt.ylabel('Implied times ',fontsize=22)
    plt.savefig(outname)
    plt.close()

msm_timescales_d = implied_timescales(sequences, lag_times, n_timescales=n_timescales, n_jobs=1,msm=MarkovStateModel(verbose=True,  reversible_type='transpose',ergodic_cutoff=0),verbose=1)
plot(msm_timescales_d,'Discrete-time MSM Relaxation Timescales','imp_times_t_erg_off3.png')

#msm_timescales_d_mle = implied_timescales(sequences, lag_times, n_timescales=n_timescales, n_jobs=1,msm=MarkovStateModel(verbose=True,  reversible_type='mle',ergodic_cutoff=1),verbose=1)
msm_timescales_d_mle = implied_timescales(sequences, lag_times, n_timescales=n_timescales, n_jobs=1,msm=MarkovStateModel(verbose=True),verbose=1)
plot(msm_timescales_d_mle,'Discrete-time MSM Relaxation Timescales MLE','imp_times_mle.png')
quit()
msm_timescales_c = implied_timescales(sequences, lag_times, n_timescales=n_timescales, n_jobs=1, msm=ContinuousTimeMSM(verbose=True),verbose=1)
plot(msm_timescales_c,'Continuous-time MSM Relaxation Timescales MLE','imp_times_c.png')

