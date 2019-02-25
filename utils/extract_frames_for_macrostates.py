import mdtraj.io as io
import numpy as np
import mdtraj as md
import multiprocessing

ref = md.load('protein_BB_A.pdb')
assigns_all = np.load('assigns.npy')

dictt = {}
ii = 0
m = ['A','B','C']

for i in range(18*3):
    f = i/3 + 1 
    dictt[i] = '/Volumes/asghar4tb/gltph/ofs_apo/wt/%d/protein_BB_200ps_%s.xtc' %(f,m[ii])
    print i, dictt[i]
    ii += 1
    if ii % 3 == 0 : ii = 0

ii = 0
for i in range(8*3):
    f = i/3 + 1
    dictt[i+18*3] = '/Volumes/asghar4tb/gltph/ofs_holo/wt/%d/protein_BB_200ps_%s.xtc' %(f,m[ii])
    print i+18*3, dictt[i+18*3]
    ii += 1
    if ii % 3 == 0 : ii = 0


ii = 0
for i in range(4*3):
    f = i/3 + 1
    dictt[i+(18+8)*3] = '/Volumes/asghar4tb/gltph/ofs_na_only/wt/%d/protein_BB_200ps_%s.xtc' %(f,m[ii])
    print i+(18+8)*3, dictt[i+(18+8)*3]
    ii += 1
    if ii % 3 == 0 : ii = 0

print "len(assigns_all):", len(assigns_all)


def save_xtc(macro_id,idd):
    xyz, lens = [], 0
    for j in range(len(assigns_all)):
	assigns = assigns_all[j] # np.loadtxt('macro12_assigns_%d.txt' %j,dtype=int)[::5]		#skip5
    	ss = np.where(assigns == macro_id)[0]
    	if len(ss) == 0:
	    continue
    	t = md.load(dictt[j],top=ref)
  	print "\t\tnumber of frames belonging to macrostate %d:" %macro_id, len(ss) 

	# trying not to save every single frame
        if len(ss) > 1000: t.xyz = t.xyz[ss[0:-1:5],:,:]
        elif len(ss) > 100: t.xyz = t.xyz[ss[0:-1:2],:,:]
        else: t.xyz = t.xyz[ss[0:-1:2],:,:]
    	xyz.append(t.xyz)

#        print "macrostate: %d trajectory: %d" %(macro_id, j), "\tt.xyz.shape", t.xyz.shape
	lens += t.xyz.shape[0]

    xyz3 = np.zeros((lens,t.xyz.shape[1],3))
    start = 0
    for k in range(len(xyz)):
	end = start + xyz[k].shape[0]
        xyz3[start:end,:,:] = xyz[k]
	start = end
    t = md.load(dictt[0] ,top=ref)
    t.xyz = xyz3
    print "Final xyz.shape (t.xyz.shape):", t.xyz.shape
    t.save_xtc2('gen%d.xtc' %(macro_id))


multi = False
listt = range(10)
if multi:
    for i in listt:
        idd = i
        p =  multiprocessing.Process(target=save_xtc,args=(i,i))
        p.start()
else:
    for i in listt:
        save_xtc(i,i)

