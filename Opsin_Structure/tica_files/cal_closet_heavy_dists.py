import mdtraj as md
import numpy as np
import mdtraj.io as io

ref = md.load('../md_files/protein.pdb')
print "number of residues:", ref.n_residues

listt = np.concatenate((range(34,60,3),range(72,99,3),range(109,137,3),range(152,172,3),range(202,233,3),range(244,274,3),range(287,310,3)))
pairs = []
for i in range(len(listt)):
    for j in range(i+1,len(listt)):
	pairs.append([listt[i],listt[j]])
pairs = np.array(pairs)
print "len(pairs):",len(pairs)

# stage 1
for i in range(4):
    traj = md.load('../md_files/stage1_xtc/protein_%d.xtc' %i,top=ref)
    print "stage1: traj, xyz.shape:", i, traj.xyz.shape
    d = md.compute_contacts(traj,contacts=pairs,scheme='closest-heavy', ignore_nonprotein=True)
    io.saveh('s1_%d.h5' %i, distances=d[0])
    io.saveh('s1_%d.h5' %i, residue_pairs=d[1])

# stage 2
for i in range(20):
    traj = md.load('../md_files/stage2_xtc/protein_%d.xtc' %i,top=ref)
    print "stage2: traj, xyz.shape:", i, traj.xyz.shape
    d = md.compute_contacts(traj,contacts=pairs,scheme='closest-heavy', ignore_nonprotein=True)
    io.saveh('s1_%d.h5' %i, distances=d[0])
    io.saveh('s1_%d.h5' %i, residue_pairs=d[1])

# stage 3
for i in range(20):
    traj = md.load('../md_files/stage3_xtc/protein_%d.xtc' %i,top=ref)
    print "stage3: traj, xyz.shape:", i, traj.xyz.shape
    d = md.compute_contacts(traj,contacts=pairs,scheme='closest-heavy', ignore_nonprotein=True)
    io.saveh('s1_%d.h5' %i, distances=d[0])
    io.saveh('s1_%d.h5' %i, residue_pairs=d[1])

# stage 4
for i in range(20):
    traj = md.load('../md_files/stage4_xtc/protein_%d.xtc' %i,top=ref)
    print "stage4: traj, xyz.shape:", i, traj.xyz.shape
    d = md.compute_contacts(traj,contacts=pairs,scheme='closest-heavy', ignore_nonprotein=True)
    io.saveh('s1_%d.h5' %i, distances=d[0])
    io.saveh('s1_%d.h5' %i, residue_pairs=d[1])

