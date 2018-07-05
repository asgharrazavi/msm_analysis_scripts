## Workflow

Step 1. Obtain the implied timescales plot by using the `implied_times2.py` script.
</br >
Step 2. Pick a Markovian lagtime and use the `hDAT_msm.py` script to build MSM.

## Comments
**MSM lagtime : 48 ns**
</br >

`assigns_all_skip20.txt` contains assignments for all of the 50 MD trajectories.
</br>
`gens_all_skip20.txt` shows the tIC 1 and tIC 2 values for each microstate on tICA landscape. These are the microstate centers.
</br>
`img_implied_times.png` shows implied timescale plot for several transition probability matrices. 
The `implied_times2.py` script can be used to get the MSM implied timescales plot.
</br>

The files `msm_*.dat` are the outputs of building an MSM:
</br>
   * `msm_populations.dat` contains thermodynamics information of the system. This is the first eigenvector of the transition propability matrix: `msm_tmat.dat`.
   * `msm_timescales.dat` contain kinetic information of the system. These are the 2nd, 3rd, etc. eigenvectors of the transition propability matrix: `msm_tmat.dat`.
   * `msm_cmat.dat` is the **count** matrix, i.e. how many times a microstate has transitioned to another microstates during the entire 50 microsecond simulations. 
`msm_tmat.dat` is obtained simply by row-normalizing the count matrix.
   * `msm_tmat.dat` is the **transition probability matrix**.
   * The eigenvalues and eigenvectors of transition probability matrix, `msm_tmat.dat`, are saved at `msm_eigenvalues.dat` and `msm_left_eigenvectors.dat` files.
   * `msm_timescales_uncertainty.dat` contains mathematical uncertainties for the MSM eigenvalues. Nore that the errors from sampling and dimentionality reductions are 
much more dominent than these mathematical uncertainties. 
   * If ergodic trimming is used, the `msm_mapping.dat` shows which microstates are trimmed (i.e., not used in calculating transition probability matrix). 
In ergodic system it would be possible to visit any microstate from any other microstate.    
