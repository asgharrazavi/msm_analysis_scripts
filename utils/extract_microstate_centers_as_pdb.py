import mdtraj.io as io
import numpy as np
import mdtraj as md
import multiprocessing

ref = md.load('/Volumes/ls/from_imac/opsin/ionized.pdb')
gens = np.loadtxt('gens.txt')
assigns = np.load('assigns.npy')

def on_tica_data():
    data = []
    for i in range(len(assigns)):    
        a = io.loadh('../../on_tica_l20_%d.h5' %i)['arr_0']
  	print i, a.shape
	data.append(a[:,0:5])
    np.save('on_tica.npy',data)
    return data

try : 
on_tica = np.load('on_tica.npy')
except: 
#on_tica = on_tica_data()

trajs, frames = [], []
for i in range(len(gens)):
    mins = []
    for j in range(len(assigns)):
	p0 = on_tica[j][:,0][::5]
	p1 = on_tica[j][:,1][::5]
	p2 = on_tica[j][:,2][::5]
	ss = (p0 - gens[i][0])**2 + (p1 - gens[i][1])**2 + (p2 - gens[i][2])**2 
        a = np.argmin( ss )
#	print i, j, gens[i], on_tica[j][a][0:3], ss[a]
	mins.append([ss[a],a])
    mins = np.array(mins)
    b = np.argmin(mins[:,0])
    print i, b, mins[b], gens[i], on_tica[b][mins[b][1]][0:3]
    trajs.append(b)
    frames.append(int(mins[b][1]))


all4 = []
for i in range(1,len(gens)):
    if trajs[i] < 4: stage = 1 ; traj = trajs[i] 
    elif 4 <= trajs[i] < 24: stage = 2 ; traj = trajs[i] - 4
    elif 24 <= trajs[i] < 44: stage = 3 ; traj = trajs[i] - 24
    elif 44 <= trajs[i] < 64: stage = 4 ; traj = trajs[i] - 44
    else: print "no mapped stage for microstate :", i, trajs[i]
    print "gen, stage, traj , frame:", i, stage, traj, frames[i]
    t = md.load('/Volumes/ls/from_imac/opsin/stage%s/ensemble_%d_skip5.xtc' %(stage,traj), top=ref)
    all4.append([i,stage,traj,frames[i]])
    a1 = assigns[trajs[i]][::5]
    print i, a1.shape, t.xyz.shape
    t.xyz = t.xyz[frames[i],:,:]
    t.save_pdb('gen_%02d.pdb' %i)
    
np.savetxt('gen_stage_traj_frame.txt',np.array(all4),fmt='%d')
quit()

def save_xtc(macro_id,idd):
    if macro_id in [1,2,4,6,7] : stage = 1 ; start = 0 ; end = 4
    if macro_id in [0,3,9] :     stage = 2 ; start = 4 ; end = 24
    if macro_id in [5,8,11] : stage = 3 ; start = 24; end = 44
    if macro_id in [10] : stage = 4 ; start = 44; end = 64
    xyz, lens = [], 0
    for j in range(start,end):
	assigns = np.loadtxt('macro12_assigns_%d.txt' %j,dtype=int)[::5]		#skip5
    	ss = np.where(assigns == macro_id)[0]
    	if len(ss) == 0:
	    continue
    	t = md.load('/Users/asr2031/Desktop/transfer/opsin/stage%d/ensemble_%d_skip5.xtc' %(stage,j-start),top=ref)
  	print "number of frames belonging to macrostate %d:" %macro_id, len(ss) 

#    	xyz.append(t.xyz[ss,:,:])
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
