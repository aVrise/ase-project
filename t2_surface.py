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
from ase.io.vasp import write_vasp, read_vasp
import numpy as np

# db1 = connect('ucells.db')
# db2 = connect('surs.db')
# a = read("cells.db@code=tio2A")

# an = 'cro2R_600_d3_T'
# a = db1.get_atoms(code=an)
a = read_vasp('POSCAR')
# a = read('/Users/jy/Downloads/TiC_mp-631_conventional_standard.cif')
# path = '/Users/jy/Library/CloudStorage/OneDrive-Personal/severfiles/202305/sta_lao/LAO_STO'
# l = ['sto_cell_opt.cif', 'lao_cell_opt.cif']
# a = read('{:s}/{:s}'.format(path,l[0]))
# a.cell=[3.905938479,3.905938479,3.905938479]
# a = a * [18,1,1]
# a.edit()
# a = sort(a)
# print(a.cell)
# exit()
# slab = surface(a,(0,0,1),1,5) * (4,4,1)
# slab = surfaces_with_termination(a, (1,0,0), layers=4,vacuum=10,termination='O',tol=1e-5) #* (3,3,1)

# slab = sort(slab)
# slab = surface(a, (1,1,0), layers=4,vacuum=10)
# view(slab)
# slab.edit()


# print([x.position for x in b])

# print(b.get_atomic_numbers)

# for i in slab:
#     db2.write(i*(1,3,1))
# b = sort(slab[1]*(2,4,1))
# fix = FixAtoms(indices=[x.index for x in b if x.position[2] < 16])
# b.set_constraint(fix)
# print(b.)

# for x in b:
#     x.position -= np.array([2.5,0.,0.])
#     cel = np.array([b.cell[0,0],b.cell[1,1],b.cell[2,2]])
#     x.position = x.position + ((x.position) < 0)*cel
#     a.extend(x)

# view(b)

# db2.write(b, code='110_'+an+'_1x2', note='Rutile RhO2 sur110 1x2')
# db2.update(db2.get(code='110_'+an+'_1x2').id,b)

# c = db2.get_atoms(name='tio2A101')
# write('tio2R.cif',b)
# write_vasp('POSCAR', a, direct=True, sort=True)
