import sys
from ase.constraints import FixAtoms
from ase.io import write
from ase.db import connect
import ase.build as bl
from ase.visualize import view
from ase.io.vasp import read_vasp,write_vasp

# a = connect("ucells.db")
a = connect('surs.db')
# a = connect('mole.db')

# b = read_vasp('t')
# b = read_vasp('POSCAR')
# b = bl.sort(b*(2,2,1))
b = a.get_atoms(code="_Bch3_h_110_iro2_1x2_k4_400_600_d3")
# view(b)

# a.write(b, code='_Bch3_h_110_tio2_1x2_k4_400_600_d3', note='ch3_h+tio2 110 k2x2 conf_B  opt')

# a.update(a.get(code='_Ach4_110_tio2_1x2_k4_400_600_d3').id,code='_Bch4_110_tio2_1x2_k4_400_600_d3')
# a.update(a.get(code='_Bch3_h_110_iro2_1x2_k4_400_600_d3').id,b)
# print(b.cell[2][2])
# print(b.get_chemical_symbols())
b=b*(3,1,1)
b.edit()
# view(b)
write('model.xyz',b)
# write_vasp('POSCAR',b,direct=True)