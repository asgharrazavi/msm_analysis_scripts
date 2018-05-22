import numpy as np
import h5py
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
from matplotlib import rcParams
rcParams.update({'figure.autolayout': True})
rcParams['axes.linewidth'] = 3
rcParams.update({'font.size': 20})

def plot(idd,name,rangee):
    plt.subplot(4,1,idd)
    s1 = []
    for i in range(rangee):
    	d = np.array(h5py.File('on_tica_l20_%s_%d.h5' %(name,i),'r').get('arr_0'))
    	s1.extend(d)
    s1 = np.array(s1)
    print s1.shape
    plt.hist2d(s1[:,0],s1[:,1],bins=100,norm=LogNorm())
    plt.xlim([-2,4])
    plt.ylim([-4,2])
#    plt.title('%s: %d frames' %(name,s1.shape[0]))

plt.figure(figsize=(7,20))
plot(1,'s1',4)
plot(2,'s2',20)
plot(3,'s3',20)
plot(4,'s4',20)
plt.xlabel('tIC 1')
plt.ylabel('tIC 2')
plt.savefig('land_tica_stages.pdf')

#plt.show()



