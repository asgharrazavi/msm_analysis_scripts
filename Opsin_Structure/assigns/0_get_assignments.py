import os,sys
import numpy as np
from msmbuilder.cluster import KMeans, KCenters
import mdtraj.io as io

cluster = KMeans(n_clusters=100,n_jobs=-1,verbose=0, max_iter=100, tol=0.0001,)


dataset = []
for i in range(4):
    a = io.loadh('../on_tica_l20_s1_%d.h5' %i)['arr_0']
    a = a[:,0:3]		# using first 3 tICs
    dataset.append(a)
    print a.shape
for i in range(20):
    a = io.loadh('../on_tica_l20_s2_%d.h5' %i)['arr_0']
    a = a[:,0:3]
    dataset.append(a)
    print a.shape
for i in range(20):
    a = io.loadh('../on_tica_l20_s3_%d.h5' %i)['arr_0']
    a = a[:,0:3]
    dataset.append(a)
    print a.shape
for i in range(20):
    a = io.loadh('../on_tica_l20_s4_%d.h5' %i)['arr_0']
    a = a[:,0:3]
    dataset.append(a)
    print a.shape

cluster.fit(dataset)
lens = [len(i) for i in dataset]
print np.array(cluster.labels_).shape
np.savetxt('gens.txt',np.array(cluster.cluster_centers_))
for i in range(64):
    np.savetxt('assigns_%d.txt' %i,np.array(cluster.labels_[i]),fmt='%d')
