from ase.db import connect
from ase.spacegroup import crystal
from ase.visualize import view
from ase.io.vasp import write_vasp

# build a connection to the datebase
db = connect('ucells.db') 

# unit cell parameters
# cell=[3.7845, 3.7845, 9.5143, 90, 90, 90] # TiO2 for example
ca=4.470
cc=2.973
cell=[ca, ca, cc, 90, 90, 90]


# build a unit cell
# x = crystal(['Cr','O'],[(0.,0.,0.),(0.306,0.306,0)],spacegroup='P42/mnm',cellpar=cell)
# x = crystal(['Ti','O'],[(0.,0.,0.),(0.,0.,0.2)],spacegroup='I41/amd',cellpar=cell)

#modify cell parameter
x = db.get_atoms(code='cro2R')
# x.cell=cell
# print(x.cell)


# view(x*(2,2,2))
db.write(x, code="cro2R_600_d3", note='Rutile CrO2 cell opt 600eV d3', url='')

# for row in db.select():
#     print(row.symbols)

# row = db.get(code='tio2R_600_d3')
# for key in row:
#     print('{0:22}: {1}'.format(key, row[key]))

# row = db.get_atoms(code='tio2A')
# view(row)

# print(db.get(code='tio2R_600_d3').id)
# db.update(db.get(code='CrO2R').id, code='cro2R') 
# a = read('cells.db@name=tio2A')
# write_vasp('POSCAR',x)

