import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def Z(r):
    #pts = [[r,0,0],[-r,0,0],[0,r,0],[0,-r,0],[0,0,r],[0,0,-r]]
    pts = [[r,0,0],[0,r,0],[0,0,r]]
    for i in range(0,r):
        for j in range(0,r):
            for k in range(0,r):
                dis = math.sqrt(i ** 2 + j ** 2 + k ** 2)
                #print(i,j,k,dis)
                if dis == r:
                    pts.append([ i, j, k])
                    #pts.append([-i, j, k])
                    #pts.append([ i,-j, k])
                    #pts.append([ i, j,-k])
                    #pts.append([-i,-j, k])
                    #pts.append([-i, j,-k])
                    #pts.append([ i,-j,-k])
                    #pts.append([-i,-j,-k])
    return pts

pts = Z(31)
arr = np.asarray(pts)
xs = arr[:,0]
ys = arr[:,1]
zs = arr[:,2]
fig, ax = plt.subplots()
ax = Axes3D(fig)
ax.scatter(xs,ys,zs)
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
plt.show()

P1 = [0,0,0]
P2 = [0,0,0]
P3 = [0,0,0]




#count = 0
#for m in range(1,51):
#    count += A(m)