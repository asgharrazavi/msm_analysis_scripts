# Comments

First we use the `pccaplus.py` script to kinetically map microstates to macrostates.
</br >
Then we use `micro_to_macro.py` to convert micro assignmnets to macro assignments. 
</br >
Finally we use `tpt.py` to obtain transition paths and fluxes.
</br >
To identify which macrostates are _sinks_ and which are _sources_ in the `tpt.py`
script, we can use the `extract_frames2.py` script to extract frames from each macrostates and visualize them.
</br >
Limited number of frames for each macrostate are saved at `macrostate_frames` folder.
You can use `../../md_files/protein.pdb` to visualize these files.
