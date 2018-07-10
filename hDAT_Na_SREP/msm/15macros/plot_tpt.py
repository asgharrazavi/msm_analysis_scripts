import matplotlib.pyplot as plt
import numpy as np
import mdtraj.io as io
from matplotlib.patches import Circle, Ellipse
import matplotlib.patches as patches
import msmbuilder.tpt as tpt
from msmbuilder.msm import ContinuousTimeMSM, MarkovStateModel
from tabulate import tabulate


fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111)

def centerss(map18,gens):
    # getting center of macrostates
    cents = []
    n_mac = int(np.max(map18+1))
    for i in range(n_mac):
        ind = [map18 == i]
        cents.append([np.mean(gens[:,0][ind]), np.mean(gens[:,1][ind])])
    return cents
        
def plot_macros(n_macros,map15,assigns22,gens,ev0,ev1,raw_data):
#    plt.hexbin(ev0, ev1, bins='log', mincnt=1, cmap="Greys")
    fmts = ['ro','bo','go','g<','mo','co','m*','c*','r*','b+','y+','y*','c*','g*','r+','r>','b>','g+']
    for i in range(n_macros):
        ind = [map15 == i]
        plt.plot(gens[:,0][ind],gens[:,1][ind],fmts[i])#colors[i])
    plt.legend(range(n_macros),ncol=18,labelspacing=0.2,numpoints=1,handletextpad=0.01,handlelength=0.5,columnspacing=0.8,shadow=True,fancybox=True,fontsize=14,bbox_to_anchor=(0.95,1.1))
    for i in range(n_macros):
        ev00, ev11 = [], []
        for j in range(50):
            dd = raw_data[j][0:len(assigns22[j])]
            ind = [assigns22[j] == i]
            if i in [3]:
                ev00.extend(dd[:,0][ind][0:-1:1])
                ev11.extend(dd[:,1][ind][0:-1:1])
            else:
                ev00.extend(dd[:,0][ind][0:-1:1])
                ev11.extend(dd[:,1][ind][0:-1:1])
        plt.plot(np.array(ev00),np.array(ev11),fmts[i],alpha=0.2)


# --------------- loading input data ---------------------------------------------
n_macro = 15
on_tica = np.load('../../tica_files/projected_on_tica_16ns_sep_skip20.npy')
gens = np.loadtxt('../gens_all_skip20.txt')
map15 = np.loadtxt('map%d_pccaplus.dat' %n_macro,dtype=int)
macro_assigns = np.loadtxt('macro15_assigns.txt', dtype=int)
ev0 = io.loadh('../../tica_files/ev0.h5')['arr_0']
ev1 = io.loadh('../../tica_files/ev1.h5')['arr_0']
# --------------------------------------------------------------------------------

plot_macros(n_macro,map15,macro_assigns,gens,ev0,ev1,on_tica)

# ---------------- build macro MSM -----------------------------------------------
# msm lagtime == 30 steps == 48 ns
msm = MarkovStateModel(lag_time=30, n_timescales=20, reversible_type='transpose', ergodic_cutoff='off', prior_counts=0, sliding_window=True, verbose=True)	
msm.fit(macro_assigns)
# --------------------------------------------------------------------------------


# ---------------- build TPT  ----------------------------------------------------
# starting macro states
sources = [10]
# ending macro states
sinks = [0,1,4]
net_flux = tpt.net_fluxes(sources, sinks, msm, for_committors=None)
print "TPT net_flux.shape:", net_flux.shape
pfold = tpt.committors(sources, sinks, msm)
paths = tpt.paths(sources, sinks, net_flux, remove_path='subtract', flux_cutoff=0.999999999)
sort = np.argsort(pfold)
total_line_width = np.sum(paths[1][0:5])
total_flux = np.sum(paths[1])
# normaize fluxes and * 100 for better visualization
fluxes = net_flux*100/total_flux
# TPT pathways
paths0 = paths[0]
# --------------------------------------------------------------------------------
                      
all_s = []
for i in paths0:
    all_s.extend(i)

pfold = np.array(pfold) * 50

# ------------------ get center of macrostates on tICA landscape -----------------
centers = centerss(map15,gens)
centers = np.array(centers)
# --------------------------------------------------------------------------------

xs = centers[:,0]
ys = centers[:,1]

r1, r2 = 0.1 , 0.12
circls = [[xs[0],ys[0],r1,r2],[xs[1],ys[1],r1*1,r2*1],[xs[2],ys[2],r1,r2],[xs[3],ys[3],r1,r2],[xs[4],ys[4],r1*1,r2*1],
          [xs[5],ys[5],r1*1,r2*1],[xs[6],ys[6],r1,r2],[xs[7], ys[7], r1*1,r2*1],[xs[8],ys[8],r1*1,r2*1],[xs[9],ys[9],r1,r2],
          [xs[10],ys[10],r1,r2],[xs[11],ys[11],r1,r2],
#	   [xs[12],ys[12],r1*1,r2*1],[xs[13],ys[13],r1,r2],[xs[14],ys[14],r1,r2],
#          [xs[15],ys[15],r1,r2],[xs[16],ys[16],r1,r2],[xs[17],ys[17],r1*1,r2*1]
         ]


for path in paths0:
    for i in range(len(path)-1):
        c1 = circls[path[i]]
        c2 = circls[path[i+1]]
        cir1 = Ellipse((c1[0],c1[1]),c1[2],c1[3],fill=False)
        cir2 = Ellipse((c2[0],c2[1]),c2[2],c2[3],fill=False)
        ax.add_patch(cir1)
        ax.add_patch(cir2)
        if fluxes[path[i]][path[i+1]] < 1 : arowprops = dict(arrowstyle="simple,head_length=1,head_width=4,tail_width=0.1", fc="k", ec="k", connectionstyle="arc3,rad=0.1",patchA=cir1,patchB=cir2)
        elif 1 < fluxes[path[i]][path[i+1]] < 10 : arowprops = dict(arrowstyle="simple,head_length=1,head_width=2,tail_width=0.1", fc="0.1", ec="0.1", connectionstyle="arc3,rad=0.1",patchA=cir1,patchB=cir2)
#        else: arowprops = dict(arrowstyle="simple,head_length=0.4,head_width=0.7,tail_width=0.1", fc="0.1", ec="0.1", connectionstyle="arc3,rad=-0.1",patchA=cir1,patchB=cir2)#,head_width=2)
        else: arowprops = dict(arrowstyle="simple", fc="0.1", ec="0.1", connectionstyle="arc3,rad=-0.1",patchA=cir1,patchB=cir2)
        ax.annotate('', xy=(xs[path[i+1]], ys[path[i+1]]), xytext=(xs[path[i]], ys[path[i]]),
                        size=fluxes[path[i]][path[i+1]], textcoords='data',xycoords = 'data', arrowprops=arowprops)

acuu_f = 0
data =[]
for j in range(len(paths[1])):
    acuu_f += paths[1][j]/float(total_flux)
    data.append([j,paths[0][j],paths[1][j],paths[1][j]/float(total_flux),acuu_f])
print tabulate(data,headers=('id','Path','Flux','Norm Flux','Accumulated Flux'),floatfmt='1.4f')

if (1):
    for i in range(len(pfold)):
        if i in np.unique(all_s):
            if i in [2,10,11] : plt.text(xs[i]-0.2,ys[i]-0.1,i, fontsize=16)
            elif i in [3,7,6] : plt.text(xs[i],ys[i]-0.25,i, fontsize=16)
            elif i in [9]: plt.text(xs[i]-0.05,ys[i]-0.25,i, fontsize=16)
            elif i in [1,4,0]: plt.text(xs[i]+0.1,ys[i]+0.05,i, fontsize=16)
            elif i in [5,8]: plt.text(xs[i]+0.05,ys[i]+0.05,i, fontsize=16)
            else: plt.text(xs[i],ys[i],i, fontsize=16)


        
#plt.xlim([-10,0])
#plt.ylim([0.5,4])
plt.savefig('img_tpt_paths.png',dpi=100)
#plt.show()
