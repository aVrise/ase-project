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
db2 = connect('surs.db')
# a = read("cells.db@code=tio2A")
an = 'cro2R_600_d3'
a = db1.get_atoms(code=an)
slab = surfaces_with_termination(a, (1,1,0), layers=4,vacuum=10,termination='O')
# view([i*(2,3,1) for i in slab])


# print([x.position for x in b])

b = sort(slab[1]*(1,2,1))
# print(b.get_atomic_numbers)
# fix = FixAtoms(indices=[x.index for x in b if x.position[2] < 13.5])
# b.set_constraint(fix)

# for i in slab:
#     db2.write(i*(1,3,1))

# view(b)

db2.write(b, code='110_'+an+'_1x2', note='Rutile CrO2 sur110 1x2 Cr_pv')
# db2.update(db2.get(code='tio2R_600_d3_110_1x2').id,b)

# c = db2.get_atoms(name='tio2A101')
# write('tio2R.cif',b)
# write_vasp('POSCAR',b ,direct=True)
