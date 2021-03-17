from icecream import ic
from ase.spacegroup import crystal
from ase.build import fcc111, add_adsorbate, bulk
from ase import Atoms
from ase.io import read, write
from ase.build import surface, molecule, sort
from ase.visualize import view
from ase.db import connect
from ase.build.surfaces_with_termination import surfaces_with_termination
from ase.io.vasp import write_vasp
import inspect

db1=connect('surs.db')
db2=connect('mole.db')
# ads=molecule('CO2')
# a = Atoms(ads.symbols, ads.positions+[5.,5.,5.], cell=[10,10,10,90,90,90]) # build a mole within a cell

# ads=db2.get_atoms(code='_ch4')
# ads.pbc = (False, False, False)
# add_adsorbate(a,ads, 2, (0,0) )

a = db1.get_atoms(code='_110_iro2_1x2_k4_400_600_d3')
b = db1.get_atoms(code='_Ach3_h_110_tio2_1x2_k4_400_600_d3')

for x in b:
    if x.symbol in ['H','C']:
        x.position += a[14].position - b[51].position
        a.extend(x)
# [print(y.symbol) for y in b if y.symbol in ['H','C'] ]
# write('co2@tio2A101.vasp',sort(a))

# view(a)
# db2.write(a, code='ch4', note='methane molecule')
write_vasp('POSCAR',sort(a),direct=True)

