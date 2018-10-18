import numpy as np
import mdtraj as md

# load inputs
ca = np.loadtxt('chol_prot_popc.txt')
ref = md.load('protein_no_chol_beta_occ.pdb')
print "number of atoms:", ref.top.n_atoms

# make a list based on ca values
s = []
for i in range(ref.n_residues):
    r = ref.top.residue(i)
    for j in range(r.n_atoms):
	s.append(ca[i])

print "number of data points:", len(s)
# len(s) should match ref.top.n_atoms

np.savetxt('tmp.txt',s,fmt='%1.2f')
