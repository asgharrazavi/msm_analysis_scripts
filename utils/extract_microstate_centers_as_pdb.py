import mdtraj.io as io
import numpy as np
import mdtraj as md
import multiprocessing

def on_tica_data():
    data = []
    for i in range(len(assigns)):    
        a = io.loadh('../../on_tica_l20_%d.h5' %i)['arr_0']
  	print i, a.shape
	data.append(a[:,0:5])
    np.save('on_tica.npy',data)
    return data

ref = md.load('/Volumes/ls/from_imac/opsin/ionized.pdb')
gens = np.loadtxt('gens.txt')
assigns = np.load('assigns.npy')


try : 
    on_tica = np.load('on_tica.npy')
except: 
    on_tica = on_tica_data()

trajs, frames = [], []
for i in range(len(gens)):
    mins = []
    for j in range(len(assigns)):
	p0 = on_tica[j][:,0][::5]
	p1 = on_tica[j][:,1][::5]
	p2 = on_tica[j][:,2][::5]
	ss = (p0 - gens[i][0])**2 + (p1 - gens[i][1])**2 + (p2 - gens[i][2])**2 
        a = np.argmin( ss )
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
