import mdtraj.io as io
import numpy as np
import mdtraj as md
import multiprocessing

ref = md.load('../../md_files/ionized.pdb')

def save_xtc(macro_id,idd):
    xyz, lens = [], 0
    for j in range(64):
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

        print "macrostate: %d trajectory: %d" %(macro_id, j), "\tt.xyz.shape", t.xyz.shape
	lens += t.xyz.shape[0]

    xyz3 = np.zeros((lens,t.xyz.shape[1],3))
    start = 0
    for k in range(len(xyz)):
	end = start + xyz[k].shape[0]
        xyz3[start:end,:,:] = xyz[k]
	start = end
    t = md.load('../../md_files/ensemble_0_skip5.xtc' ,top=ref)
    t.xyz = xyz3
    print "final xyz.shape (t.xyz.shape):", t.xyz.shape
    t.save_xtc2('gen%d.xtc' %(macro_id))


multi = False
if multi:
    for i in [0,1,3,4,5,8,10]:
        idd = i
        p =  multiprocessing.Process(target=save_xtc,args=(i,i))
        p.start()
else:
    for i in [0,1,3,4,5,8,10]:
        save_xtc(i,i)

