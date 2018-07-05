## Workflow

Step 1. Use `pccaplus.py` script to kinetically lump microstates into macrostate.
</br >
Step 2. Convert microstate assignments to macrostate assignments using `micro_to_macro.py`.
</br >
Step 3. Build MSM and perform transition path theory (TPT) analysis on macrostate level using the `tpt.py` script.

## Comments

**macro MSM lagtime : 48 ns**
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

