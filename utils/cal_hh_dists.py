"""
Script for calculating hydrophobic-hydrophobic interactions in MD simulations
"""

import numpy as np
import mdtraj as md
import mdtraj.io as io
import h5py

def pairs(amin1,amin2):
    p = []
    for i in amin1:
	for j in amin2:
	    p.append([i,j])
    return np.array(p)

def dists(traj,ref,atom_pairs):
    d = md.compute_distances(traj, atom_pairs, periodic=True, opt=True)
    return d
  
def _save(outname,amin1,amin2,data):
    pairs2 = pairs(amin1,amin2)
    with h5py.File(outname, 'a') as hf:
     for i in range(len(pairs2)):
	hf.create_dataset('%s--%s' %(ref.top.atom(pairs2[i][0]),ref.top.atom(pairs2[i][1])), data=np.float16(data[:,i]))

def save_dists(outname,traj_path,ref):
    traj = md.load(traj_path,top=ref)
    t, r = traj, ref
    rr, rk, rd, re, r4, r5, r6, r7, r8 = dists(t,r,pairs(ala,ala)), dists(t,r,pairs(ala,ile)), dists(t,r,pairs(ala,leu)), dists(t,r,pairs(ala,phe)), dists(t,r,pairs(ala,trp)), dists(t,r,pairs(ala,tyr)), dists(t,r,pairs(ala,val)), dists(t,r,pairs(ala,pro)), dists(t,r,pairs(ala,gly))    
    _save(outname,ala,ala,rr); _save(outname,ala,ile,rk); _save(outname,ala,leu,rd); _save(outname,ala,phe,re); _save(outname,ala,trp,r4); _save(outname,ala,tyr,r5); _save(outname,ala,val,r6); _save(outname,ala,pro,r7); _save(outname,ala,gly,r8)
    kk, kd, ke, k4, k5, r6, r7, r8 = dists(t,r,pairs(ile,ile)), dists(t,r,pairs(ile,leu)), dists(t,r,pairs(ile,phe)), dists(t,r,pairs(ile,trp)), dists(t,r,pairs(ile,tyr)), dists(t,r,pairs(ile,val)), dists(t,r,pairs(ile,pro)), dists(t,r,pairs(ile,gly))   
    _save(outname,ile,ile,kk); _save(outname,ile,leu,kd); _save(outname,ile,phe,ke); _save(outname,ile,trp,k4); _save(outname,ile,tyr,k5); _save(outname,ile,val,r6); _save(outname,ile,pro,r7); _save(outname,ile,gly,r8)
    dd, de, d4, d5, r6, r7, r8 = dists(t,r,pairs(leu,leu)), dists(t,r,pairs(leu,phe)), dists(t,r,pairs(leu,trp)), dists(t,r,pairs(leu,tyr)), dists(t,r,pairs(leu,val)), dists(t,r,pairs(leu,pro)), dists(t,r,pairs(leu,gly))   
    _save(outname,leu,leu,dd); _save(outname,leu,phe,de); _save(outname,leu,trp,d4); _save(outname,leu,tyr,d5); _save(outname,leu,val,r6); _save(outname,leu,pro,r7); _save(outname,leu,gly,r8)
    ee, e4, e5, r6, r7, r8 = dists(t,r,pairs(phe,phe)), dists(t,r,pairs(phe,trp)), dists(t,r,pairs(phe,tyr)), dists(t,r,pairs(phe,val)), dists(t,r,pairs(phe,pro)), dists(t,r,pairs(phe,gly))   
    _save(outname,phe,phe,ee); _save(outname,phe,trp,e4); _save(outname,phe,tyr,e5); _save(outname,phe,val,r6); _save(outname,phe,pro,r7); _save(outname,phe,gly,r8)
    s44, s45, r6, r7, r8 = dists(t,r,pairs(trp,trp)), dists(t,r,pairs(trp,tyr)), dists(t,r,pairs(trp,val)), dists(t,r,pairs(trp,pro)), dists(t,r,pairs(trp,gly))   
    _save(outname,trp,trp,s44); _save(outname,trp,tyr,s45); _save(outname,trp,val,r6); _save(outname,trp,pro,r7); _save(outname,trp,gly,r8)
    s55, r6, r7, r8 = dists(t,r,pairs(tyr,tyr)), dists(t,r,pairs(tyr,val)), dists(t,r,pairs(tyr,pro)), dists(t,r,pairs(tyr,gly))   
    _save(outname,tyr,tyr,s55); _save(outname,tyr,val,r6); _save(outname,tyr,pro,r7); _save(outname,tyr,gly,r8)
    r6, r7, r8 = dists(t,r,pairs(val,val)), dists(t,r,pairs(val,pro)), dists(t,r,pairs(val,gly))   
    _save(outname,val,val,r6); _save(outname,val,pro,r7); _save(outname,val,gly,r8)
    r7, r8 = dists(t,r,pairs(pro,pro)), dists(t,r,pairs(pro,gly))   
    _save(outname,pro,pro,r7); _save(outname,pro,gly,r8)
    r8 = dists(t,r,pairs(gly,gly))   
    _save(outname,gly,gly,r8)
 
# load refrence pdb
ref_path = '/Users/asr2031/Desktop/transfer/dDAT_WT_ensemble_stampede/ionized.pdb'
ref = md.load(ref_path)

# parse hydrophobic residues
ala = ref.top.select('protein and resname ALA and name CB')
ile = ref.top.select('protein and resname ILE and name CD1')
leu = ref.top.select('protein and resname LEU and name CG')
phe = ref.top.select('protein and resname PHE and name CZ')
trp = ref.top.select('protein and resname TRP and name CE2')
tyr = ref.top.select('protein and resname TYR and name CZ')

val = ref.top.select('protein and resname VAL and name CB')
pro = ref.top.select('protein and resname PRO and name CG')
gly = ref.top.select('protein and resname GLY and name CA')


for i in range(50):
    print "working on trajectory:\t", i
    traj_path = '/Users/asr2031/Desktop/transfer/dDAT_WT_ensemble_stampede/1to1025_skip20/traj%d_whole_1to1025_skip20.xtc'  %i
    save_dists('traj%d_hh.h5' %i,traj_path,ref)




