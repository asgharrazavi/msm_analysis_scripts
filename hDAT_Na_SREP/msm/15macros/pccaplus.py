import numpy as np
import msmbuilder.lumping as lump
from msmbuilder.msm import ContinuousTimeMSM, MarkovStateModel

assigns = np.loadtxt('../assigns_all_skip20.txt' ,dtype=int)
msm = MarkovStateModel(lag_time=30, n_timescales=20, reversible_type='transpose', ergodic_cutoff='off', prior_counts=0, sliding_window=True, verbose=True)
msm.fit(assigns)

tmat = np.loadtxt('../msm_tmat.dat')
m = lump.PCCAPlus.from_msm(msm,n_macrostates=10)
np.savetxt('map10_pccaplus.dat',m.microstate_mapping_,fmt='%d')
