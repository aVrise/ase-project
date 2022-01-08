from ase.build import bulk, surface, fcc100, fcc110, fcc111, hcp0001, bcc110, molecule
from ase.calculators.emt import EMT
from ase.eos import calculate_eos
from ase.db import connect
from ase.io.vasp import read_vasp,write_vasp
from ase.io import write
from ase.constraints import FixAtoms
import sys, os
import numpy as np

# atoms = bulk('Ag', 'fcc',a=4.208, cubic=True)
# atoms = bulk('Au', 'fcc',a=4.20, cubic=True)
# atoms = bulk('Pt', 'fcc',a=3.9898, cubic=True)
# atoms = bulk('Pd', 'fcc',a=3.9796, cubic=True)
# atoms = bulk('Cu', 'fcc',a=3.6840, cubic=True)
# atoms = bulk('Ni', 'fcc',a=3.557, cubic=True)
# atoms = bulk('Ir', 'fcc',cubic=True)
# slab = surface(atoms,(2,1,1),6,7.5) * (2,4,1)

# slab = fcc111('Ni',(1,2,4),a=3.557,vacuum=7.5,orthogonal=True) 
# slab = fcc100('Ni',(1,1,4),a=3.557,vacuum=7.5,orthogonal=True) 
# slab = fcc111('Cu',(4,4,3),a=3.6840,vacuum=7.5,orthogonal=True)
# slab = fcc111('Ag',(4,4,3),a=4.208,vacuum=7.5,orthogonal=True)
# slab = fcc111('Au',(4,4,3),a=4.20,vacuum=7.5,orthogonal=True) 
# slab = fcc111('Pt',(1,2,3),a=3.9898,vacuum=7.5,orthogonal=True)
# slab = fcc111('Pd',(4,4,3),a=3.9796,vacuum=7.5,orthogonal=True)
# slab = bcc110('V',(4,4,3),a=3.001,vacuum=7.5,orthogonal=True)
# slab = hcp0001('Ti',(4,4,3),a=2.9225, c=4.6329, vacuum=7.5,orthogonal=True)
# slab = hcp0001('Ti',(4,4,3),a=2.9446836397465557, c=4.6715667106969461, vacuum=7.5,orthogonal=True)

slab = fcc111('Ni',(3,3,3),a=3.5517,vacuum=7.5,orthogonal=True) 
# slab = fcc111('Cu',(3,3,3),a=3.6769,vacuum=7.5)
# slab = fcc111('Ag',(3,3,3),a=4.2072,vacuum=7.5)
# slab = fcc111('Au',(3,3,3),a=4.1971,vacuum=7.5) 
# slab = fcc111('Pt',(3,3,3),a=3.9899,vacuum=7.5)
# slab = fcc111('Pd',(3,3,3),a=3.9819,vacuum=7.5)
# slab = fcc111('Rh',(3,3,3),a=3.8457,vacuum=7.5)
# slab = fcc111('Ir',(3,3,3),a=3.8844,vacuum=7.5)

# slab = fcc100('Ni',(3,3,3),a=3.5517,vacuum=7.5) 
# slab = fcc100('Cu',(3,3,3),a=3.6769,vacuum=7.5)
# slab = fcc100('Ag',(3,3,3),a=4.2072,vacuum=7.5)
# slab = fcc100('Au',(3,3,3),a=4.1971,vacuum=7.5) 
# slab = fcc100('Pt',(3,3,3),a=3.9899,vacuum=7.5)
# slab = fcc100('Pd',(3,3,3),a=3.9819,vacuum=7.5)
# slab = fcc100('Rh',(3,3,3),a=3.8457,vacuum=7.5)
# slab = fcc100('Ir',(3,3,3),a=3.8844,vacuum=7.5)

# fix = FixAtoms(indices=[x.index for x in slab if x.position[2] < 9])
# slab.set_constraint(fix)

# print(slab.cell)
# atoms = molecule('CO')
# slab.edit()
# atoms.edit()


# write('Ni111.cif',slab)
# write_vasp('POSCAR',slab,sort=True,direct=True)
# write_vasp('POSCAR',atoms,sort=True,direct=True)

# ref = read_vasp('POSCAR')
# write_vasp('POSCAR1',ref,sort=True,direct=True)
# b = read_vasp("/Users/jy/severfiles/202105/CONTCAR")
# for _1 in b:
#     if _1.symbol != 'Cu':
#         _1.position = _1.position * np.array([ref.cell[0,0],ref.cell[1,1],ref.cell[2,2]]) / np.array([b.cell[0,0],b.cell[1,1],b.cell[2,2]])
#         # _1.position[0] = 4.455
#         # _1.position[1] = 4.289
#         ref += _1
# ref.edit()
# write_vasp('/Users/jy/severfiles/202106/POSCAR_ch4-mno2_spins',ref,sort=True,direct=True)

# path0="/Users/jy/severfiles/202111/Cu111_NRR_CONT/"
# # path0="/Users/jy/severfiles/202111/"
# with open(path0+"list",'r') as f1:
#     for _ in range(24):
#         ref_1 = ref.copy()
#         a = f1.readline().strip()
#         # print(a[14:] == 'n') 
#         b = read_vasp(path0+a)
#         # if a[14:] in ['oh', 'o', 'n', 'h', 'noh', 'nh']:
#         # if a[14:] in [ 'nho', 'nh2', 'nh2o', 'nhoh']:
#         # if a[14:] == 'oh':
#             # pos1 = b[b.get_chemical_symbols().index('N')].position
#             # dd = pos - pos1 * np.array([ref.cell[0,0],ref.cell[1,1],ref.cell[2,2]]) / np.array([b.cell[0,0],b.cell[1,1],b.cell[2,2]])
#         for _1 in b:
#             if _1.symbol != 'Cu':
#                 _1.position = _1.position * np.array([ref.cell[0,0],ref.cell[1,1],ref.cell[2,2]]) / np.array([b.cell[0,0],b.cell[1,1],b.cell[2,2]])
#                 # _1.position[0] = 4.455
#                 # _1.position[1] = 4.289
#                 ref_1 += _1
#         ref_1.edit()
#         write_vasp('/Users/jy/severfiles/202111/POSCAR_Rh111_'+a[13:],ref_1,sort=True,direct=True)

# with open("/Users/jy/severfiles/202106/list",'r') as f1:
#     for _ in range(24):
#         a = f1.readline().strip()
#         b = read_vasp("/Users/jy/severfiles/202106/"+a)
#         write_vasp('/Users/jy/severfiles/202106/ni210/'+a,b,sort=True,direct=True)

# with open("/Users/jy/severfiles/202111/list",'r') as f1:
#     for _ in range(9):
#         a = f1.readline().strip()
#         b = read_vasp("/Users/jy/severfiles/202111/"+a)
#         write_vasp('/Users/jy/severfiles/202111/'+a+'s',b,sort=True,direct=True)
