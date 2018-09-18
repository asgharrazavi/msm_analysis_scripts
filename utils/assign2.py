import os,sys
import numpy as np
from msmbuilder.cluster import KMeans, KCenters
import mdtraj.io as io


cluster = KMeans(n_clusters=100,n_jobs=-1,verbose=0, max_iter=100, tol=0.0001,)


dataset = []
for i in range(50):
    a = io.loadh('./on_tica_l16ns_%d.h5' %i)['arr_0']
    print a.shape
    inds = [0,1]
    a = a[:,inds]
    dataset.append(a)
    print a.shape

cluster.fit(dataset)
print np.array(cluster.labels_).shape
    np.savetxt('assigns_%d_skip20.txt' %i,np.array(cluster.labels_[i]),fmt='%d')
np.savetxt('gens_all_skip20.txt',np.array(cluster.cluster_centers_))
#np.savetxt('gens_id2.txt',np.array(cluster.cluster_ids_))
