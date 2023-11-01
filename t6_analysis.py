import sys,os
from ase.constraints import FixAtoms
from ase.io import write
from ase.db import connect
import ase.build as bl
from ase.visualize import view
from ase.io.vasp import read_vasp, write_vasp
import numpy as np

# a = connect("ucells.db")
a = connect('surs.db')
# a = connect('mole.db')

l = ['ti','ir','mn','cr','ru','rh']
# b = read_vasp('t')
# b = read_vasp('POSCAR')
# b = bl.sort(b*(2,2,1))
# b = a.get_atoms(code="_0ch3h_110_cro2R_600_d3_T_1x2")
# b = a.get_atoms(id=58)

# fix = FixAtoms(indices=[x.index for x in b if x.position[2] < 16])
# b.set_constraint(fix)

# view(b)
# print(b.cell)
# a.write(b, code='_0ch3h_110_cro2R_600_d3_T_1x2', note='0ch3h Cro2 110 k2x2 opt Ueff=3eV Cr_pv')

# a.update(a.get(code='_Ach4_110_tio2_1x2_k4_400_600_d3').id,code='_Bch4_110_tio2_1x2_k4_400_600_d3')
# a.update(58,b,code='_1ch3h_110_cro2R_600_d3_T_1x2',note='1ch3h Cro2 110 k2x2 opt Ueff=3eV Cr_pv')
# print(b.cell[2][2])
# print(b.get_chemical_symbols())
# b=b*(3,1,1)
# b.edit()
# view(b)
# write('model.xyz',b)
# write('/Users/jy/severfiles/202103/movie.xyz',b)
# write_vasp('POSCAR',b,direct=True)

# c = []
# for i in l[1:]:
#     b = a.get_atoms(code='_0ch3h_110_'+i+'o2R_600_d3_T_1x2')
#     c.append(b.copy())
# view(c)

for row in a.select():
    if not 'ch' in row['code'] :
        continue
    b = a.get_atoms(code=row['code'])
    ic = 99
    ia = list(set(b.get_chemical_symbols()) - set(['H','C','O']))[0]
    for ie,ib in enumerate(b):
        if ib.symbol == ia:
            ic = min(ic,b.get_distance(0,ie))
    print(row['code'],ic)
print(b.get_distance(0,15))
