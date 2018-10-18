import numpy as np
import mdtraj as md

ca = np.loadtxt('chol_prot_popc.txt')

ref = md.load('protein_no_chol_beta_occ.pdb')
print "n atoms:",ref.top.n_atoms

s = []
for i in range(ref.n_residues):
    r = ref.top.residue(i)
    for j in range(r.n_atoms):
	s.append(ca[i])

print "n data:", len(s)
np.savetxt('tmp.txt',s,fmt='%1.2f')

