#!/usr/bin/env python3
import sys
import numpy as np
import matplotlib.pyplot as plt
from ase.io import read,write
from ase.io.vasp import read_vasp, write_vasp
from ase.build import sort
from ase.constraints import FixAtoms

def cov(b,c,d,e):
    global a
    print(cosv(a[c].position - a[b].position,a[d].position - a[b].position))
    print(cosv(a[c].position - a[b].position,a[e].position - a[b].position))

def cosv(a,b):
    return np.dot(a,b)/np.linalg.norm(a)/np.linalg.norm(b)

def pos(x):
    global a
    return np.dot(x.position,np.linalg.inv(a.cell))

# a = read_vasp('/Users/jy/severfiles/202105/pdos/ch4-rho2/POSCAR')
# a = read('/Users/jy/severfiles/202105/pdos/ch4-rho2/1.xyz')
a = read('/Users/jy/severfiles/202108/oso2.xyz')
a = read('/Users/jy/Library/CloudStorage/OneDrive-Personal/severfiles/202106/big_rho2_rutile.xyz')
# a = read('/Users/jy/Library/CloudStorage/OneDrive-Personal/severfiles/202108/ruo2_reduced.xyz')
# a = read('POSCAR')

A = 380
B = 706
C = 1537
D = 1097
A = 251 ; B = 634 ; C = 1433 ; D = 1046 # iro2
A = 369 ; B = 756 ; C = 1551 ; D = 1165 # rho2
# lattice

# # AC = a[907].position - a[866].position
# # BD = a[867].position - a[908].position
# # cov(317,215,669,656)
# # cov(275,297,1105,1035)
print(np.linalg.norm(a[D].position - a[A].position),np.linalg.norm(a[C].position - a[B].position))
print(np.linalg.norm(a[B].position - a[A].position),np.linalg.norm(a[C].position - a[D].position))

# rotation cleavage

b = -1e-3
bs = np.sin(b/180*np.pi)
bc = np.cos(b/180*np.pi)
c = np.array([[bc,bs,0],[-bs,bc,0],[0,0,1]])
f1=f2=f3=f4=0
d = 0.8
for _ in range(9000000000):
    a.positions = np.dot(a.positions,c.T)
    if abs(a[D].position[0] - a[A].position[0]) < 1e-2 and f1 == 0:
        a.positions[a.positions[:,0]<a[A].position[0]-d] *= 0
        f1 = 1
    if abs(a[C].position[0] - a[B].position[0]) < 1e-2 and f2 == 0:
        a.positions[a.positions[:,0]>a[C].position[0]+d] *= 0
        f2 = 1
    if abs(a[C].position[1] - a[D].position[1]) < 1e-2 and f3 == 0:
        a.positions[a.positions[:,1]>a[D].position[1]+d] *= 0
        f3 = 1
    if abs(a[B].position[1] - a[A].position[1]) < 1e-2 and f4 == 0:
        a.positions[a.positions[:,1]<a[B].position[1]-d] *= 0
        f4 = 1
    if f1*f2*f3*f4 == 1:
        break
# print(f1,f2,f3,f4)
xx = a[B].position-a[A].position
ctt = xx[0]/np.linalg.norm(xx)
stt = np.sqrt(1-ctt**2)
a.positions = np.dot(a.positions,np.array([[ctt,stt,0],[-stt,ctt,0],[0,0,1]]))
a.cell = np.vstack((a[B].position-a[A].position,a[D].position-a[A].position,np.array([[0,0,31.9392856444035083]])))
a.positions[:,:2] -= a[A].position[:2]
del a[a.positions[:,2]==0]
print(sort(a).symbols)

# remove repeat
d = 0.01
for i in a:
    if i.position[2] == 0:
        continue
    for j in a:
        if i.index == j.index:
            continue
        if j.position[2] == 0:
            continue
        disth = np.mod(np.abs(pos(i) - pos(j)),1.)
        if np.linalg.norm(disth) < d or ((abs(disth[0])<d and abs(disth[1])> 1-d) or (abs(disth[0]) > 1-d and abs(disth[1])<d) or (abs(disth[0]) > 1-d and abs(disth[1])>1-d)):
            j.position *= 0

del a[a.positions[:,2]==0]
print(sort(a).symbols)

fix = FixAtoms(indices=[x.index for x in a if x.position[2] < 16])
a.set_constraint(fix)

# remove redundent 
# c_index = 768
# for i in a:
#     if i.symbol == 'C' and i.index != c_index:
#         i.position *= 0
#     if i.symbol == 'H' and np.linalg.norm(a[c_index].position - i.position) > 2:
#         i.position *= 0
# del a[a.positions[:,2]==0]

a.edit()
# write('/Users/jy/severfiles/202105/pdos/ch4-tio2/2.xyz',a)
# write_vasp('/Users/jy/severfiles/202107/POSCAR_ch4-iro2',a,direct=True,sort=True)
# write_vasp('/Users/jy/Library/CloudStorage/OneDrive-Personal/severfiles/202108/POSCAR_ruo2225_ch4_0',a,direct=True,sort=True)
# AC = a[98].position - a[141].position
# BD = a[193].position - a[95].position
# tt = a[111].position - a[141].position
# # print(cosv(AC,BD),np.cos(105*np.pi/180))
# points = []
# for i in a:
#     if int(i.position[2]) == 11 and int(i.position[0]) in [5,11] :
#         points.append(i.position)

# n=2
# dat=[]
# for i in points:
#     for j in range(n):
#         for k in range(n):
#             if j ==0 and k == 0:
#                 continue
#             # AX = i - a[141].position + np.array([a.cell[0,0],a.cell[1,1],a.cell[2,2]])*np.array([j,k,0])
#             BX = i - a[141].position + np.array([a.cell[0,0],a.cell[1,1],a.cell[2,2]])*np.array([-j,k,0])
#             # if cosv(BD,BX) > 0.999:
#             #     # print(i,j,k,cosv(AC,AX))
#             #     print(i,j,k,cosv(BD,BX))
# print(a[141].position)
            
