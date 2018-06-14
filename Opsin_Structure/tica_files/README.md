# Workflow
step1: use `cal_closet_heavy_dists.py` to calculate tICA parameters.
<br />  
step2: use `get_tica_obj_simple.py` to get tICA object.
<br />  
step3: use `project_on_tica_simple.py` to project tICA parameters on tICA eigenvectors.
<br />  

# Comments
Some of the `on_tica_l20_??.h5` files are not here because of large sizes. 
`on_tica_l20_50.h5 to on_tica_l20_63.h5` are projection of **stage 4** of the simulations on tICA reaction coordinates.
<br />  
The files: `ev0.h5`  and  `ev1.h5`  are projection of all of the MD simulation data on tICA **1st** and **2nd** eigenvectors.
These files can be used to plot MD projections on tICA 1st and 2nd eigenvectors (i.e. reaction coordinates).
The `land_tica_stages.pdf` shows projection of each statge of simulations on these two reaction coordinates.
<br />  
`tic_cont_zoom.png` and `tic_cont_all.png` show contribution of each tICA eigenvector to total dynamics captured by tICA. 
These contributions are normalized and accumulated and calculated using the `plot_tica_contributions.py` script.
These contributions are calculated based on the references below (the original tICA papers):
<br />  

<a href="https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.72.3634">Separation of a Mixture of Independent Signals Using Time Delayed Correlations</a>
,L. Molgedey and H. G. Schuster, Phys. Rev. Lett. 72, 3634, (1994) 
<br />  
<a href="https://aip.scitation.org/doi/abs/10.1063/1.3554380">Slow dynamics in protein fluctuations revealed by time-structure based independent component analysis: The case of domain motions</a>
,Yusuke Naritomi and Sotaro Fuchigami,  The Journal of Chemical Physics 134, 065101 (2011); doi: 10.1063/1.3554380


