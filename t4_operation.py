import sys,os
from ase import Atoms
from ase.constraints import FixAtoms
from ase.io import write
from ase.db import connect
import ase.build as bl
from ase.visualize import view
from ase.io.vasp import read_vasp,write_vasp
import numpy as np


# a = connect("ucells.db")
a = connect('surs.db')
# a = connect('mole.db')
# a = connect('coop.db')

# b = read_vasp('t')
# b = read_vasp('POSCAR')
# b = bl.sort(b*(2,2,1))
# b = a.get_atoms(code="_0ch4_110_mno2R_600_d3_T_2x4")
# b = a.get_atoms(id=84)
  
# fix = FixAtoms(indices=[x.index for x in b if x.position[2] < 16])
# b.set_constraint(fix)

# view(b)
# print(b.cell[2,2]/b.cell[0,0])
# a.write(b, code='_0ch3h_110_ruo2R_600_d3_T_2x4', note='0ch3h Ruo2 110 k2x2 opt U=2eV Ru_pv AF')
# a.write(b, code='_ni_4x4', note='ni 3l1b k3x3')

# a.update(a.get(code='_0ch4_110_iro2R_600_d3_T_2x4').id,code='_Bch4_110_tio2_1x2_k4_400_600_d3')
# a.update(84,note='0ch4 RuO2 110 k2x2 opt U=2eV Ru_pv AF')
# print(b.cell[2][2])
# print(b.get_chemical_symbols())
# b=b*(3,1,1)
# b.edit()
# view(b)
# write('../_out/model.xyz',b)
# write('/Users/jy/severfiles/202103/movie.xyz',b)
# write_vasp('POSCAR',b,direct=True)

# copy neb structures
# os.system('rm neb/*/*')
# for i in ['01', '02', '03', '04', '05', '06']:
#     b = read_vasp('neb1/'+i+'/CONTCAR')
#     c = a.get_atoms(code='_110_rho2R_600_d3_T_1x2')
#     for x in b:
#         if x.symbol in ['H','C']:
#             x.position += c[46].position - b[51].position
#             cel = np.array([b.cell[0,0],b.cell[1,1],b.cell[2,2]])
#             x.position = x.position - ((x.position - cel) > 0)*cel
#             c.extend(x)
#     c.edit()
#     write_vasp('neb/'+i+'/POSCAR',bl.sort(c),direct=True)

# supercell
# for i in ['_110_ruo2R_600_d3_T_1x2','_0ch4_110_ruo2R_600_d3_T_1x2','_0ch3h_110_ruo2R_600_d3_T_1x2']:
#     b = a.get_atoms(code=i)
#     c = []
#     d = Atoms()
#     for ii in range(len(b)):
#         if b[ii].symbol in ['H', 'C']:
#             # if b[ii].position[0] < 3:
#             #     b[ii].position[0] += b.cell[0,0]
#             c.append(ii)
#             d.append(b[ii])
#     del b[c]
#     b = bl.sort(b*(2,2,1))
#     b.extend(d)
#     view(b)
#     write_vasp('../_out/POSCAR'+i,b,direct=True,sort=True)


# add configuration
b = a.get_atoms(code='_0ch3h_110_ruo2R_600_d3_T_1x2')
blist = [0,1,2,3,4,51,34]
# c = a.get_atoms(code='_110_iro2R_600_d3_2x4')
c = read_vasp('POSCAR')
clist = [182,45]
dd = c[173].position - b[42].position
del c[clist]
for i in blist:
    # if b[i].symbol == 'O':
    #     b[i].position = b[i].position + dd + b.cell[0]
    b[i].position = b[i].position + dd
    c.extend(b[i])
# c.edit()
# write_vasp('POSCAR',c,sort=True,direct=True)

# add transition
# b = a.get_atoms(code='_0ch4-0ch3h_110_ruo2R_600_d3_T_1x2')
# blist = [38,14,29,11,15,13,0,1,2,3,4]
# bz = b[42].position - b[blist[0]].position
# c = a.get_atoms(code='_110_ruo2R_600_d3_T_2x4')
# c = read_vasp('POSCAR')
# clist = [182,95,111,110,94,45]
# # cz = c[133].position - c[clist[0]].position
# # dd = c[5].position - b[10].position - bz + cz
# dd = c[173].position - b[49].position
# del c[clist]
# for i in blist:
#     # if b[i].symbol in ['C','H','O'] and b[i].position[0] > 5:
#     #     b[i].position[0] = b[i].position[0] - b.cell[0,0]
#     b[i].position = b[i].position + dd
#     c.extend(b[i])
# c.edit()
# write_vasp('POSCAR',c,sort=True,direct=True)

# element substitute
# b = read_vasp('POSCAR')
b = c
for i in range(len(b)):
    if b[i].symbol == 'Ru':
        # dis = [1.444,2.887,7.218,8.661] # Mn
        # dis = [1.555,3.111,7.777, 9.332] # Ru
        # if min([abs(b[i].position[1] - x) for x in dis]) < 0.5:
        b[i].symbol = 'Os'
view(b)
# write_vasp('../_out/pos',b,direct=True,sort=True)
write_vasp('POSCAR1',b,direct=True,sort=True)