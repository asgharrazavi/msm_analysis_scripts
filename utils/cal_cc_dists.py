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
	print '\t\t', '%s--%s' %(ref.top.atom(pairs2[i][0]),ref.top.atom(pairs2[i][1]))
	hf.create_dataset('%s--%s' %(ref.top.atom(pairs2[i][0]),ref.top.atom(pairs2[i][1])), data=np.float16(data[:,i]))

def save_dists(outname,traj_path,ref):
    traj = md.load(traj_path,top=ref)
    t, r = traj, ref
    rr, rk, rd, re, r4, r5 = dists(t,r,pairs(arg,arg)), dists(t,r,pairs(arg,lys)), dists(t,r,pairs(arg,asp)), dists(t,r,pairs(arg,glu)), dists(t,r,pairs(arg,sap4)), dists(t,r,pairs(arg,sap5))    
    _save(outname,arg,arg,rr)
    _save(outname,arg,lys,rk)
    _save(outname,arg,asp,rd)
    _save(outname,arg,glu,re)
    _save(outname,arg,sap4,r4)
    _save(outname,arg,sap5,r5)
    kk, kd, ke, k4, k5 = dists(t,r,pairs(lys,lys)), dists(t,r,pairs(lys,asp)), dists(t,r,pairs(lys,glu)), dists(t,r,pairs(lys,sap4)), dists(t,r,pairs(lys,sap5))   
    _save(outname,lys,lys,kk)
    _save(outname,lys,asp,kd)
    _save(outname,lys,glu,ke)
    _save(outname,lys,sap4,k4)
    _save(outname,lys,sap5,k5)
    dd, de, d4, d5 = dists(t,r,pairs(asp,asp)), dists(t,r,pairs(asp,glu)), dists(t,r,pairs(asp,sap4)), dists(t,r,pairs(asp,sap5))   
    _save(outname,asp,asp,dd)
    _save(outname,asp,glu,de)
    _save(outname,asp,sap4,d4)
    _save(outname,asp,sap5,d5)
    ee, e4, e5 = dists(t,r,pairs(glu,glu)), dists(t,r,pairs(glu,sap4)), dists(t,r,pairs(glu,sap5))   
    _save(outname,glu,glu,ee)
    _save(outname,glu,sap4,e4)
    _save(outname,glu,sap5,e5)
    s44, s45 = dists(t,r,pairs(sap4,sap4)), dists(t,r,pairs(sap4,sap5))   
    _save(outname,sap4,sap4,s44)
    _save(outname,sap4,sap5,s45)
    s55 = dists(t,r,pairs(sap5,sap5))   
    _save(outname,sap5,sap5,s55)
 

# load reference pdb
ref_path = '/Users/asr2031/Desktop/transfer/dDAT_WT_ensemble_stampede/ionized.pdb'
ref = md.load(ref_path)

# parse all charged residues
arg = ref.top.select('protein and resname ARG and name CZ')
lys = ref.top.select('protein and resname LYS and name NZ')
asp = ref.top.select('protein and resname ASP and name CG')
glu = ref.top.select('protein and resname GLU and name CD')

# parse charged lipid molecules
sap4 = ref.top.select('segname SAP4 and name P')
sap5 = ref.top.select('segname SAP5 and name P')


# load trajectories
for i in range(50):
    print "working on trajectory:\t", i
    traj_path = '/Users/asr2031/Desktop/transfer/dDAT_WT_ensemble_stampede/1to781_skip20/traj%d_whole_1to781_skip20.xtc'  %i
    save_dists('traj%d_cc_t.h5' %i,traj_path,ref)




