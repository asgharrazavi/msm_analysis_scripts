import os,sys
import numpy as np
from msmbuilder.cluster import KMeans, KCenters
import mdtraj.io as io


# clusterin object
cluster = KMeans(n_clusters=100,n_jobs=-1,verbose=0, max_iter=100, tol=0.0001,)

# load projected on tICA data
on_tica = np.load('on_tica.npy')

# which tICA projections be used for clusterin
inds = [0,1]
dataset = []
for i in range(len(on_tica)):
    dataset.append(on_tica[:,inds])

cluster.fit(dataset)
np.save('assigns.npy',cluster.labels_)
np.savetxt('gens.txt',np.array(cluster.cluster_centers_))
