# Workflow

Step 1. Project all simulation data on tICA reaction coordinates.  
<br />
Step 2. Cluster all simulation dat based on their tICA values to obtain microstates and assign each frame to a microstate. (assignments are in the `assigns` folder).  
<br />
Step 3. Use `implied_times2.py` to calculate MSM implied timescales for a series of MSM lag-times. 
<br />  
Step 4. Choose a proper MSM lag-time and use `opsin_msm.py` to get MSM eigenvalues, eigenvectors, transition probability matrix, etc.
<br />  
Step 5. Lump microstates to creat `macrostates` using the `pccaplus.py` in the `12macros` folder. 
<br />  


# Comments

**msm lagtime: 40 ns**

MSM could be build on a _macrostate_ level for better visualization of 
metastable states and transitions among them and obtaining flux values that capture conformational
transitions in a dynamics system. See `12macros` folder for _macro-level_ MSM for the Opsin.


