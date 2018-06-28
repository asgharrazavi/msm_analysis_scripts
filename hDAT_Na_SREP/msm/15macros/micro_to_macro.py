import os,sys
import mdtraj.io as io
import numpy as np

map15 = np.loadtxt('map15_pccaplus.dat')

def mapp(micro_assigns,macro_map):
    n_macros = int(np.max(macro_map)) + 1
    macro_assigns = np.ones(micro_assigns.shape)  * -100
    for i in range(n_macros):
	ind_map = np.where(macro_map == i)[0]
	for m in ind_map:
		ind = (micro_assigns == m)
		macro_assigns[ind] = i
    if [-100] in macro_assigns:
	print "not all micro assignments are converted"
    return macro_assigns 

micro_assigns = np.loadtxt('assigns_all_skip20.txt',dtype=int)
macro_assigns = mapp(micro_assigns,map15)
print "i, micro_assigns.shape:", i, micro_assigns.shape
np.savetxt('macro15_assigns.txt', macro_assigns, fmt='%d')
