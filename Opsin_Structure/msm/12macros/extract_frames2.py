import mdtraj.io as io
import numpy as np
import mdtraj as md
import multiprocessing

ref = md.load('../../md_files/ionized.pdb')

def save_xtc(macro_id,idd):
#    if macro_id in [1,2,4,6,7] : stage = 1 ; start = 0 ; end = 4
#    if macro_id in [0,3,9] :     stage = 2 ; start = 4 ; end = 24
#    if macro_id in [5,8,11] : stage = 3 ; start = 24; end = 44
#    if macro_id in [10] : stage = 4 ; start = 44; end = 64
    xyz, lens = [], 0
    for j in range(start,end):
	assigns = np.loadtxt('macro12_assigns_%d.txt' %j,dtype=int)[::5]		#skip5
    	ss = np.where(assigns == macro_id)[0]
    	if len(ss) == 0:
	    continue
    	t = md.load('../../md_files/stage%d/ensemble_%d_skip5.xtc' %(stage,j-start),top=ref)
  	print "number of frames belonging to macrostate %d:" %macro_id, len(ss) 
	# trying not to save every single frame
        if len(ss) > 1000: t.xyz = t.xyz[ss[0:-1:30],:,:]
        elif len(ss) > 100: t.xyz = t.xyz[ss[0:-1:10],:,:]
        else: t.xyz = t.xyz[ss[0:-1:2],:,:]
    	xyz.append(t.xyz)
        print macro_id, j, "t.xyz.shape", t.xyz.shape
	lens += t.xyz.shape[0]
    xyz3 = np.zeros((lens,t.xyz.shape[1],3))
    start = 0
    for k in range(len(xyz)):
	end = start + xyz[k].shape[0]
        xyz3[start:end,:,:] = xyz[k]
	start = end
    print "xyz3.shape:", xyz3.shape
    t = md.load('/Users/asr2031/Desktop/transfer/opsin/stage1/ensemble_0_skip5.xtc' ,top=ref)
    t.xyz = xyz3
    print "final xyz.shape (t.xyz.shape):", t.xyz.shape
    t.save_xtc2('gen%d.xtc' %(macro_id))


for i in [0,1,3,4,5,8,10]:
    save_xtc(i,i)
#    idd = i
#    p =  multiprocessing.Process(target=save_xtc,args=(i,i))
#    p.start()
