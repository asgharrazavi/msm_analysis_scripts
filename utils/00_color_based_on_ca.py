import numpy as np
import mdtraj as md

ca = np.loadtxt('chol_prot_popc2.txt')

ref = md.load('protein.pdb')
print "nubmer of atoms:",ref.top.n_atoms

# save a text file for color values ifor each residue that can be used in VMD for visualization
s = []
for i in range(ref.n_residues):
    r = ref.top.residue(i)
    for j in range(r.n_atoms):
	s.append(ca[i])

print "number of data points (must macth number of atoms):", len(s)
np.savetxt('tmp.txt',s,fmt='%1.2f')

