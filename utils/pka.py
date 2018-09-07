import os,sys,commands
import mdtraj as md
import numpy as np
import matplotlib.pyplot as plt

def get_pka(pka_file,residue):
    pka = commands.getoutput(''' tail -n 420 %s  | head -n 380 | grep "%s"  | awk '{print $4}' ''' %(pka_file,residue))
    pka = commands.getoutput(''' cat %s  | grep "  %s"  | awk '{print $4}' ''' %(pka_file,residue))
    try: return float(pka)    
    except: return 0.0

# load trajectory
t = md.load_dcd('../prot-ion-coor-all.dcd',top='../prot-ion.pdb')
n_frames = t.xyz.shape[0]
xyz = t.xyz

# calculate pKa values for every 5 frame
for i in range(0,n_frames,5):
    print i
    t.xyz = xyz[i]
    t.save_pdb('a')
    os.system('sed "3d" a > %d-ns.pdb' %(i+1))
    os.system('propka31 %d-ns.pdb -i "A:327,A:779,A:804,A:808,A:926,A:954" ' %(i+1))
    os.system('rm a %d-ns.pdb *propka_input' %(i+1))

# extract pKa values for some important residues as plot them
d804, d808, d926, e327, e779 = np.zeros(n_frames), np.zeros(n_frames), np.zeros(n_frames), np.zeros(n_frames), np.zeros(n_frames)
for i in range(n_frames):
    d804[i] = (get_pka('%d-ns.pka' %(i+1),'ASP 804'))
    d808[i] = (get_pka('%d-ns.pka' %(i+1),'ASP 808'))
    d926[i] = (get_pka('%d-ns.pka' %(i+1),'ASP 926'))
    e327[i] = (get_pka('%d-ns.pka' %(i+1),'GLU 327'))
    e779[i] = (get_pka('%d-ns.pka' %(i+1),'GLU 779'))

d804, d808, d926, e327, e779 = np.array(d804), np.array(d808), np.array(d926), np.array(e327), np.array(e779)
np.savetxt('d804.txt',np.array(d804))
np.savetxt('d808.txt',np.array(d808))
np.savetxt('d926.txt',np.array(d926))
np.savetxt('e327.txt',np.array(e327))
np.savetxt('e779.txt',np.array(e779))

d804, d808, d926, e327, e779 = d804[d804 > 1], d808[d808 > 1], d926[d926 > 1],  e327[e327 > 1], e779[e779 > 1]
e327, e779 = e327[e327 > 1], e779[e779 > 1]

means = [np.mean(d804), np.mean(d808), np.mean(d926), np.mean(e327), np.mean(e779)]
stds = [np.std(d804), np.std(d808), np.std(d926), np.std(e327), np.std(e779)]

plt.errorbar(range(5),means,yerr=stds,fmt='o')
plt.xticks(range(5),['D804','D808','D926','E327','E779'],fontsize=18)
plt.xlim([-1,5])
plt.xlabel('Residue',fontsize=18)
plt.ylabel('Average pKa in %d frames' %n_frames,fontsize=14)
plt.yticks(fontsize=18)
plt.title('3KDP')
plt.savefig('pka.pdf')


