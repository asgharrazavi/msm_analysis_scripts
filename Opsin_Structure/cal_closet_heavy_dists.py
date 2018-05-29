import mdtraj as md
import numpy as np
import mdtraj.io as io

ref = md.load('../../protein.pdb')
print "number of residues:", ref.n_residues

listt = np.concatenate((range(34,60,3),range(72,99,3),range(109,137,3),range(152,172,3),range(202,233,3),range(244,274,3),range(287,310,3)))
pairs = []
for i in range(len(listt)):
    for j in range(i+1,len(listt)):
	pairs.append([listt[i],listt[j]])
pairs = np.array(pairs)
print "len(pairs):",len(pairs)

for i in range(4):
    print i
#    traj = md.load('../protein_%d_skip5.xtc' %i,top=ref)
    traj = md.load('../protein_%d.xtc' %i,top=ref)
    print traj.xyz.shape
    d = md.compute_contacts(traj,contacts=pairs,scheme='closest-heavy', ignore_nonprotein=True)
    io.saveh('t%d.h5' %i, distances=d[0])
    io.saveh('t%d.h5' %i, residue_pairs=d[1])

print d
