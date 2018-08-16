import matplotlib.pyplot as plt
import numpy as np
import mdtraj.io as io
from matplotlib.patches import Circle, Ellipse
import matplotlib.patches as patches
import msmbuilder.tpt as tpt
from msmbuilder.msm import ContinuousTimeMSM, MarkovStateModel
from tabulate import tabulate

# ========================================== functions ==========================
def get_macro_centers(n_macro,map15,gens):
   print "\tgetting macrostate centers..."
    cents = []
    for i in range(n_macro):
        ind = [map15 == i]
        cents.append([np.mean(gens[:,0][ind]), np.mean(gens[:,1][ind])])
    return cents
        
def plot_macros(n_macros,map15,assigns22,gens,ev0,ev1,raw_data):
    print "\tplotting macrostate tICA space..."
    plt.hexbin(ev0, ev1, bins='log', mincnt=1, cmap="Greys")
    fmts = ['ro','bo','go','g<','mo','co','m*','c*','r*','b+','y+','y*','c*','g*','r+','r>','b>','g+']
    for i in range(n_macros):
        ind = [map15 == i]
        plt.plot(gens[:,0][ind],gens[:,1][ind],fmts[i])#colors[i])
    plt.legend(range(n_macros),ncol=n_macros,labelspacing=0.2,numpoints=1,handletextpad=0.01,handlelength=0.5,columnspacing=0.8,shadow=True,fancybox=True,fontsize=18,bbox_to_anchor=(0.95,1.1))
    for i in range(n_macros):
        ev00, ev11 = [], []
        for j in range(50):
            dd = raw_data[j][0:len(assigns22[j])]
            ind = [assigns22[j] == i]
            ev00.extend(dd[:,0][ind][0:-1:1])
            ev11.extend(dd[:,1][ind][0:-1:1])
        plt.plot(np.array(ev00),np.array(ev11),fmts[i],alpha=0.3,markersize=8)
    plt.xlim([np.min(ev0)-0.1,np.max(ev0)+0.1])
    plt.ylim([np.min(ev1)-0.1,np.max(ev1)+0.1])
# ================================================================================


# --------------- loading input data ---------------------------------------------
print "loading input data..."
n_macro = 15
on_tica = np.load('../../tica_files/projected_on_tica_16ns_sep_skip20.npy')
gens = np.loadtxt('../gens_all_skip20.txt')
map15 = np.loadtxt('map%d_pccaplus.dat' %n_macro,dtype=int)
macro_assigns = np.loadtxt('macro15_assigns.txt', dtype=int)
ev0 = io.loadh('../../tica_files/ev0.h5')['arr_0']
ev1 = io.loadh('../../tica_files/ev1.h5')['arr_0']
# --------------------------------------------------------------------------------

# ---------------- build macro MSM -----------------------------------------------
print "building macrostate MSM..."
# msm lagtime == 30 steps == 48 ns
msm = MarkovStateModel(lag_time=30, n_timescales=20, reversible_type='transpose', ergodic_cutoff='off', prior_counts=0, sliding_window=True, verbose=True)	
msm.fit(macro_assigns)
# --------------------------------------------------------------------------------

# ---------------- build TPT  ----------------------------------------------------
print "building TPT..."
# starting macro states
sources = [14]
# ending macro states
sinks = [1,3,5,7]
net_flux = tpt.net_fluxes(sources, sinks, msm, for_committors=None)
print "TPT net_flux.shape:", net_flux.shape
pfold = tpt.committors(sources, sinks, msm)
paths = tpt.paths(sources, sinks, net_flux, remove_path='subtract', flux_cutoff=0.999999999)
sort = np.argsort(pfold)
total_line_width = np.sum(paths[1][0:5])
total_flux = np.sum(paths[1])
# normaize fluxes and * 100 for better visualization
fluxes = net_flux * 100/total_flux
# --------------------------------------------------------------------------------

# ------------------ get center of macrostates on tICA landscape -----------------
centers = get_macro_centers(n_macro,map15,gens)
centers = np.array(centers)
# --------------------------------------------------------------------------------

# ---------- circles to represent macro states ---------
xs = centers[:,0]
ys = centers[:,1]

r1, r2 = 0.1 , 0.12
circls = []
for i in range(n_macro):
    circls.append([xs[i],ys[i],r1,r2])
# ------------------------------------------------------

# -------------------- plot pathways on tICA landscape ----------------------------
fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111)

# first plot tICA landscape and macrostates
plot_macros(n_macro,map15,macro_assigns,gens,ev0,ev1,on_tica)

# all pathways
n_paths = -1
for path in paths[0][0:n_paths]:
    for i in range(len(path)-1):
        c1 = circls[path[i]]
        c2 = circls[path[i+1]]
        cir1 = Ellipse((c1[0],c1[1]),c1[2],c1[3],fill=False)
        cir2 = Ellipse((c2[0],c2[1]),c2[2],c2[3],fill=False)
        ax.add_patch(cir1)
        ax.add_patch(cir2)
	# editing arrow properties from some of the pathways for better viualization
        if fluxes[path[i]][path[i+1]] < 1 : arowprops = dict(arrowstyle="fancy,head_length=2,head_width=2,tail_width=1", fc="k", ec="0.3", connectionstyle="arc3,rad=0.1",patchA=cir1,patchB=cir2)
        elif 1 < fluxes[path[i]][path[i+1]] < 10 : arowprops = dict(arrowstyle="fancy,head_length=2,head_width=2,tail_width=1", fc="0.1", ec="0.3", connectionstyle="arc3,rad=0.1",patchA=cir1,patchB=cir2)
        else: arowprops = dict(arrowstyle="fancy", fc="0.1", ec="0.1", connectionstyle="arc3,rad=-0.1",patchA=cir1,patchB=cir2)
        ax.annotate('', xy=(xs[path[i+1]], ys[path[i+1]]), xytext=(xs[path[i]], ys[path[i]]),
                        size=fluxes[path[i]][path[i+1]], textcoords='data',xycoords = 'data', arrowprops=arowprops)
# --------------------------------------------------------------------------------

# --------------------- print TPT pathways ---------------------------------------
acuu_f = 0
data =[]
for j in range(len(paths[1])):
    acuu_f += paths[1][j]/float(total_flux)
    data.append([j,paths[0][j],paths[1][j],paths[1][j]/float(total_flux),acuu_f])
print tabulate(data,headers=('id','Path','Flux','Norm Flux','Accumulated Flux'),floatfmt='1.4f')
# --------------------------------------------------------------------------------

# --------------------- label macrostates on tICA landscape ----------------------
all_s = []
for i in paths[0]:
    all_s.extend(i)
for i in range(len(pfold)):
    if i in np.unique(all_s):
        if i in [2,10,11] : plt.text(xs[i]-0.2,ys[i]-0.1,i, fontsize=16)
        elif i in [3,7,6] : plt.text(xs[i],ys[i]-0.25,i, fontsize=16)
        elif i in [9]: plt.text(xs[i]-0.05,ys[i]-0.25,i, fontsize=16)
        elif i in [1,4,0]: plt.text(xs[i]+0.1,ys[i]+0.05,i, fontsize=16)
        elif i in [5,8]: plt.text(xs[i]+0.05,ys[i]+0.05,i, fontsize=16)
        else: plt.text(xs[i],ys[i],i, fontsize=16)
# --------------------------------------------------------------------------------


plt.savefig('img_tpt_paths.png',dpi=100)
