## Workflow

Step 1. Use `pccaplus.py` script to kinetically lump microstates into macrostate.
Step 2. Convert microstate assignments to macrostate assignments using `micro_to_macro.py`.
Step 3. Build MSM and transition path theory (TPT) on macrostate level.

## Comments

**macro MSM lagtime : 48 ns**
</br >

`macro15_assigns.txt` contains **macrostate** assignments for all of the 50 MD trajectories. 
The script `micro_to_macro.py` is used to generate these.
</br>
`gens_all_skip20.txt` shows the tIC 1 and tIC 2 values for each microstate on tICA landscape. These are the microstate centers.
</br>
`img_implied_times.png` shows implied timescale plot for several transition probability matrices. 
The `implied_times2.py` script can be used to get the MSM implied timescales plot.
