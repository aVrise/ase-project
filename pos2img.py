'''
time python3 ase-project/pos2img.py /Users/jy/Library/CloudStorage/OneDrive-Personal/severfiles/202211/active_sites_stt/POSCAR_100079_*
'''


from collections import Counter
import matplotlib
matplotlib.use('TkAgg')

import multiprocessing as mp
import matplotlib.pyplot as plt
from matplotlib.patches import Circle as circ
import numpy as np
from ase.io import vasp
from ase.data import covalent_radii
from ase.geometry import cell_to_cellpar
from ase.build import sort as asort
import json
import sys

def read_pos(filepath, ax):

    a = vasp.read_vasp(filepath) 

    zmin = np.min(a.positions[:,2])
    a.positions -= np.array([[0,0,zmin]])

    celx = round(a.cell[0,0],2)
    cely = round(a.cell[1,1],2)
    celx_shift = round(a.cell[1,0],2)
    cely_shift = round(a.cell[0,1],2)
    # print(a.cell[:2,:2],celx,cely)
    a *= (3,3,1)
    # a.edit()
    # cellpar = cell_to_cellpar(a.cell)

    a = asort(a,tags=a.positions[:,2])

    for atom in a:
        r = atom.number
        l = round(0.89 * covalent_radii[r],2) #* 100
        z = int(round(atom.position[2],1) * 10)
        # print(atom.position)
        ax.add_patch(circ([round(x,2) for x in atom.position[:2]],l,color=rgb_to_hex(r,z,0),aa=False))

    return celx, cely, round(a.cell[0,0],2), round(a.cell[1,1],2), celx_shift, cely_shift


def rgb_to_hex(r, g, b):
  return ('#{:02X}{:02X}{:02X}').format(r, g, b)

# print(rgb_to_hex(255, 165, 1))
def count_sum(data):
    ele = set(data[:,0]) - set([0])
    d_ele = {}
    for i in ele:
        a = np.int8(data.copy()[(data[:,0]==i)][:,1])
        b = Counter(a)
        c = {}
        for ii,jj in b.items():
            c[int(ii)] = int(jj)
        # print(b,c)
        # ca = b.keys()
        # cb = b.values()
        # print(ca,cb)
        # print(c)
        d_ele[int(i)] = c #dict([[int(ca[x]),int(cb[x])] for x in range(len(ca))])
        
    # print(d_ele)
    return d_ele

fig, ax = plt.subplots(1)
plt.xticks([])
plt.yticks([])
plt.xlabel([])
plt.ylabel([])
plt.axis('off')
fig.set_dpi(100)
fig.tight_layout(pad=0)

# print(len(sys.argv[1:]))
al = []

for i in sys.argv[1:]:

    celx, cely, acelx, acely, xshift, yshift = read_pos(i, ax)

    # print(celx,cely)
    icelx = int(round(celx*100,0)) ; icely = int(round(cely*100,0))
    fig.set_size_inches(icelx/100+0.0001,icely/100+0.0001)
    plt.xlim(icelx/100+xshift, 2*icelx/100+xshift)
    plt.ylim(icely/100+yshift, 2*icely/100+yshift)
    # print(plt.xlim()[1]-plt.xlim()[0])
    fig.canvas.draw()
    # print(celx,cely,fig.canvas.get_width_height()[::-1] + (3,))
    # plt.savefig('_out/dedup/'+i.split('/')[-1]+'.tiff')#, transparent = False, dpi = 100, pad_inches=0.1,bbox_inches='tight')
    # print(fig.canvas.get_width_height()[::-1] + (3,))
    # plt.show()
    # print(fig.canvas.get_width_height()[::-1] + (3,),icelx,icely)
    data = np.frombuffer(fig.canvas.tostring_rgb(), dtype=np.uint8)
    # data = data.reshape(fig.canvas.get_width_height()[::-1] + (3,))   
    data = data.reshape((icelx*icely),3)
    # print(fig.canvas.get_width_height()[::-1] + (3,))
    a = count_sum(data)
    a['file'] = i.split('/')[-1]
    al.append(a)

    # print(al)
    
    # print(a.keys())

    # print(' '.join([i.split('/')[-1]]+len(a.keys())+[str(x) for x in a.keys()]+[str(x) for x in a.values()]))
    # plt.xlim(0, acelx)
    # plt.ylim(0, acely)
    # plt.show()
    # ax.clear()
    ax.patches = []

# print(al)

ii = i.split('/')[-1].split('_')[1]
print(ii)
with open('_out/dedup/'+ii+'.json', 'w') as f:
    json.dump(al,f)

# print(fig.canvas.get_width_height())


# print(data.shape)

# print(plt.xlim()[1],plt.ylim()[1])
# plt.savefig('_out/pos2img.jpg', transparent = False, dpi = my_dpi,pad_inches=0.1,bbox_inches='tight')
# plt.show()
