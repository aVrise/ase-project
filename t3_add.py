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

db1=connect('surfaces.db')
ads=molecule('CO2')
a=db1.get_atoms(name='tio2A101')
add_adsorbate(a,ads,3,(2.5,3.8))
# write('co2@tio2A101.vasp',sort(a))
view(a)
# write_vasp('co2vasp@tioA101_poscar',sort(a),direct=True)

