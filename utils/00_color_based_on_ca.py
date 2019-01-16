import numpy as np
import mdtraj as md

ca = np.loadtxt('chol_prot_popc2.txt')

ref = md.load('protein.pdb')
print "nubmer of atoms:",ref.top.n_atoms

# saving a text file for color values that can be used in visualization
s = []
for i in range(ref.n_residues):
    r = ref.top.residue(i)
    for j in range(r.n_atoms):
	s.append(ca[i])

print "n data:", len(s)
np.savetxt('tmp.txt',s,fmt='%1.2f')

