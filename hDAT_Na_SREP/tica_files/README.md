## Workflow

Step 1. Use `build_tICA.py` to build tICA object.
</br >
Step 2. Use `project_on_tica.py` to project MD simulations data on tICA eigenvectors and obtain tICA landscape.
</br >
Step 3. Use `plot_tica_contributions.py` to estimate how much each tICA eigenvector contributes to total dynamics captured by tICA parameters.



## Comments


##### tICA lagtime: 16 ns
</br >

The numpy file `projected_on_tica_16ns_sep_skip20.npy` contains projection of MD simulation data on all tICA eigenvectors for all 50 MD simulations trajectories. Frames are saved every 1.6 ns.
The numpy file `projected_on_tica_16ns_sep.npy` contains more MD frames that are projected on tICA eigenvectors.
</br >

The file `img_tica_landscape.png` shows the tICA landscape generated from above two numpy files.
</br >

`ev0.h5` and `ev1.h5` are projection of MD simulations data on tICA 1st and 2nd eigenvectors.
The file `img_tica_landscapes_eigenvalues.png` shows a projection of all of the 50 MD trajectories on tICA eigenvectors.
</br >

`img_parameter_contribution_for_tica_eigenvectors.png` shows that _1st_ tICA reaction coordinates captures Na+/Na2 movement, whereas, the _2nd_ tICA coordinate captures intracellular gate dynamics. 
This plot is generated using the `plot_parameter_contribution_for_tica_eigenvectors.py` script.
</br >

`img_trajs_on_tica.pdf` shows how tICA landscape is explored during simulation time for several trajectories in which Na+/Na2 eventually is released to the intracellular environment.
</br >

`img_tic_cont_zoom.png` shows accumulated contribution of each tICA eigenvector to total dynamics captured by tICA parameters. See Refrences below:

   *   <a href="https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.72.3634">Separation of a Mixture of Independent Signals Using Time Delayed Correlations</a>
, L. Molgedey and H. G. Schuster, Phys. Rev. Lett. 72, 3634, (1994) 
   *   <a href="https://aip.scitation.org/doi/abs/10.1063/1.3554380">Slow dynamics in protein fluctuations revealed by time-structure based independent component analysis: The case of domain motions</a>
, Yusuke Naritomi and Sotaro Fuchigami,  The Journal of Chemical Physics 134, 065101 (2011); doi: 10.1063/1.3554380


