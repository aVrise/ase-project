# from icecream import ic
# from ase.spacegroup import crystal
# from ase.build import fcc111, add_adsorbate, bulk
# from ase import Atoms
from ase.io import read, write
from ase.build import surface, molecule, sort
from ase.visualize import view
from ase.db import connect
from ase.build.surfaces_with_termination import surfaces_with_termination
from ase.constraints import FixAtoms
from ase.io.vasp import write_vasp

db1 = connect('ucells.db')
# db2 = connect('surfaces.db')
# a = read("cells.db@code=tio2A")
a = db1.get_atoms(code='tio2A')
slab = surfaces_with_termination(a, (1,0,1), layers=4,vacuum=7.5,termination='O')
b = sort(slab[0]*(1,3,1))


# print([x.position for x in b])
fix = FixAtoms(indices=[x.index for x in b if x.position[2] < 13.5])
b.set_constraint(fix)

# for i in slab:
#     db2.write(i*(1,3,1))

# view(slab)

# db2.write(b, name='tio2A101')

# c = db2.get_atoms(name='tio2A101')
# write('tio2A.vasp',c)
write_vasp('co2vasp@tioA101_poscar',b ,direct=True)
