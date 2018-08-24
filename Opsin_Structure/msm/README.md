# Workflow

step1: project all simulation data on tICA reaction coordinates.
<br />
step2: cluster all simulation dat based on their tICA values to obtain microstates and assign each frame to a microstate.  
(assignments are in the `assigns` folder)
<br />
step3: use `implied_times2.py` to calculate MSM implied timescales for a series of MSM lag-times.
<br />  
step4: choose a proper MSM lag-time and use `opsin_msm.py` to get MSM eigenvalues, eigenvectors, transition probability matrix, etc.
<br />  
step5: lump microstates to creat `macrostates` using the `pccaplus.py` in the `12macros` folder. 
<br />  


# Comments

**msm lagtime: 40 ns**

MSM could be build on a _macrostate_ level for better visualization of 
metastable states and transitions among them and obtaining flux values that capture conformational
transitions in a dynamics system. See `12macros` folder for _macro-level_ MSM for the Opsin.


