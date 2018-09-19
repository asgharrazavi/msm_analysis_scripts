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
#	print '\t\t', '%s--%s' %(ref.top.atom(pairs2[i][0]),ref.top.atom(pairs2[i][1]))
	hf.create_dataset('%s--%s' %(ref.top.atom(pairs2[i][0]),ref.top.atom(pairs2[i][1])), data=np.float16(data[:,i]))
#	io.saveh2(outname,'%s--%s' %(ref.top.atom(pairs2[i][0]),ref.top.atom(pairs2[i][1])),np.float16(data[:,i]))

def save_dists(outname,traj_path,ref):
    traj = md.load(traj_path,top=ref)
    t, r = traj, ref
    rr, rk, rd, re, r4, r5, r6 = dists(t,r,pairs(gln,gln)), dists(t,r,pairs(gln,asn)), dists(t,r,pairs(gln,his)), dists(t,r,pairs(gln,ser)), dists(t,r,pairs(gln,thr)), dists(t,r,pairs(gln,cys)), dists(t,r,pairs(gln,met))
    _save(outname,gln,gln,rr); _save(outname,gln,asn,rk); _save(outname,gln,his,rd); _save(outname,gln,ser,re); _save(outname,gln,thr,r4); _save(outname,gln,cys,r5); _save(outname,gln,met,r6)
    kk, kd, ke, k4, k5, r6 = dists(t,r,pairs(asn,asn)), dists(t,r,pairs(asn,his)), dists(t,r,pairs(asn,ser)), dists(t,r,pairs(asn,thr)), dists(t,r,pairs(asn,cys)), dists(t,r,pairs(asn,met))
    _save(outname,asn,asn,kk); _save(outname,asn,his,kd); _save(outname,asn,ser,ke); _save(outname,asn,thr,k4); _save(outname,asn,cys,k5); _save(outname,asn,met,r6)
    dd, de, d4, d5, r6 = dists(t,r,pairs(his,his)), dists(t,r,pairs(his,ser)), dists(t,r,pairs(his,thr)), dists(t,r,pairs(his,cys)), dists(t,r,pairs(his,met))
    _save(outname,his,his,dd); _save(outname,his,ser,de); _save(outname,his,thr,d4); _save(outname,his,cys,d5); _save(outname,his,met,r6)
    ee, e4, e5, r6 = dists(t,r,pairs(ser,ser)), dists(t,r,pairs(ser,thr)), dists(t,r,pairs(ser,cys)), dists(t,r,pairs(ser,met))
    _save(outname,ser,ser,ee); _save(outname,ser,thr,e4); _save(outname,ser,cys,e5); _save(outname,ser,met,r6)
    s44, s45, r6 = dists(t,r,pairs(thr,thr)), dists(t,r,pairs(thr,cys)), dists(t,r,pairs(thr,met))
    _save(outname,thr,thr,s44); _save(outname,thr,cys,s45); _save(outname,thr,met,r6)
    s55, r6 = dists(t,r,pairs(cys,cys)), dists(t,r,pairs(cys,met))
    _save(outname,cys,cys,s55); _save(outname,cys,met,r6)
    r6 = dists(t,r,pairs(met,met))
    _save(outname,met,met,r6)
 

ref_path = '/Users/asr2031/Desktop/transfer/dDAT_WT_ensemble_stampede/ionized.pdb'
ref = md.load(ref_path)

gln = ref.top.select('protein and resname GLN and name CD')
asn = ref.top.select('protein and resname ASN and name CG')
his = ref.top.select('protein and resname HIS and name CE1')
ser = ref.top.select('protein and resname SER and name OG')
thr = ref.top.select('protein and resname THR and name OG1')
cys = ref.top.select('protein and resname CYS and name SG')
met = ref.top.select('protein and resname MET and name SD')

for i in range(50):
    print "working on trajectory:\t", i
    traj_path = '/Users/asr2031/Desktop/transfer/dDAT_WT_ensemble_stampede/1to1025_skip20/traj%d_whole_1to1025_skip20.xtc'  %i
    save_dists('traj%d_pp.h5' %i,traj_path,ref)




