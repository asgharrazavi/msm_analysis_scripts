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

Slow dynamics in protein fluctuations revealed by time-structure based independent component analysis: The case of domain motions

