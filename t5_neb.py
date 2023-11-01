import sys, os
from ase.constraints import FixAtoms
from ase.io import write
from ase.db import connect
import ase.build as bl
from ase.visualize import view
from ase.io.vasp import read_vasp,write_vasp
from ase.neb import NEB
from ase import Atoms


a = connect('surs.db')
c1 = a.get_atoms(code='_0ch4_110_mno2R_600_d3_T_1x2')
c2 = a.get_atoms(code='_0ch3h_110_mno2R_600_d3_T_1x2')
images=6
# for i in [2,4,13,14,29,30,42,43,50]:
#     c2[i].position[0] = c2[i].position[0] - c2.cell[0][0]
# write_vasp('POSCAR',c2)
# c2 = read_vasp('POSCAR')
# c3 = c2.copy()
# c2[1] = c3[4]
# c2[3] = c3[1]
# c2[4] = c3[3] 

c = [c1.copy() for x in range(images+1)] + [c2.copy()]
b = NEB(c)
b.interpolate()
# # b.interpolate(method='idpp')

os.system('rm -rf neb/[0-9]*')
for i in range(len(c)): 
    os.system('mkdir neb/{:0>2d}'.format(i))
    write_vasp('neb/{:0>2d}/POSCAR'.format(i),c[i],direct=True)

# view(c)


