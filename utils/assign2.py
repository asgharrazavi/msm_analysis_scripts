import os,sys
import numpy as np
from msmbuilder.cluster import KMeans, KCenters
import mdtraj.io as io


cluster = KMeans(n_clusters=100,n_jobs=-1,verbose=0, max_iter=100, tol=0.0001,)


dataset = []
for i in range(50):
    a = io.loadh('./on_tica_l16ns_%d.h5' %i)['arr_0']
    inds = [0,1]
    a = a[:,inds]
    dataset.append(a)

cluster.fit(dataset)
np.save('assigns.npy',cluster.labels_)
np.savetxt('gens.txt',np.array(cluster.cluster_centers_))
