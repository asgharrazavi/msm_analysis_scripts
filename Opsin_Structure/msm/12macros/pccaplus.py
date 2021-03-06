import numpy as np
import msmbuilder.lumping as lump
from msmbuilder.msm import ContinuousTimeMSM, MarkovStateModel

assigns = []
for i in range(64):
    assigns.append(np.loadtxt('../../assigns/assigns_%d.txt' %i ,dtype=int))
# MSM lagtime: 500 steps * 80 ps = 40ns
msm = MarkovStateModel(lag_time=500, n_timescales=20, reversible_type='transpose', ergodic_cutoff='off', prior_counts=0, sliding_window=True, verbose=True)
msm.fit(assigns)

m = lump.PCCAPlus.from_msm(msm,n_macrostates=12)
np.savetxt('map12_pccaplus.dat',m.microstate_mapping_,fmt='%d')
