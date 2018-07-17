## Workflow

Step 1. Use `pccaplus.py` script to kinetically lump microstates into macrostate.
</br >
Step 2. Convert microstate assignments to macrostate assignments using `micro_to_macro.py`.
</br >
Step 3. Build MSM and perform transition path theory (TPT) analysis on macrostate level using the `tpt.py` script.

## Comments

**Macro MSM lagtime : 48 ns**
</br >
**Number of macro states : 15**

</br >

`macro15_assigns.txt` contains **macrostate** assignments for all of the 50 MD simulation trajectories. 
The script `micro_to_macro.py` is used to generate these.
</br>

`img_macrostates.png` shows macrostates on the tICA landscape.
</br>

`tpt.py` prints out pathways and corresponding fluxes.
</br>

The `macro_*.xtc` files contain several randomly selected frames for each macrostate. The `ionized.psf` file in the `../../md_files` directory can be used to visualize these macrostates. 
The `extract_frames2.xtc` is used to extract these frames. 
Due to the large disc sizes the original MD simulations trajectories are not on this repository. 
</br>

The `plot_tpt.py` script plots TPT pathways and can be used to plot TPT identified pathways on the tICA landscape. 
For the hDAT system these pathways are saved in `img_tpt_first_7_paths.png` and `img_tpt_paths.png` files.
</br>

The `plot_tpt.py` script is not limited to hDAT and can be used to map TPT pathways on tICA landscape for any system, as long as you have the following input files:
   * `gens.txt` : microstate centers on tICA landscape.
   * `map15_pccaplus.dat` : identifies which microstates belong to each macrostate.
   * `ev0.h5` : projection of all of the MD simulations data on the first tICA reaction coordinate.
   * `ev1.h5` : projection of all of the MD simulations data on the second tICA reaction coordinate.
   * `projected_on_tica_16ns_sep_skip20.npy` : projection of individual trajectories on tICA space.
   * `macro_assignments.txt` : assignments for each of the simulations trajectories for macrostates. 
