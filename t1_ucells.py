from ase.db import connect
from ase.spacegroup import crystal
from ase.visualize import view

# build a connection to the datebase
db = connect('ucells.db') 

# unit cell parameters
tio2A_a=3.7845 
tio2A_c=9.5143
tio2A_alpha=90

# build a unit cell
tio2_bulk = crystal(['Ti','O'],[(0.,0.,0.),(0.,0.,0.2)],spacegroup=141,cellpar=[tio2A_a,tio2A_a,tio2A_c,tio2A_alpha,tio2A_alpha,tio2A_alpha])
# tio2_bulk = crystal(['Ti','O'],[(0.,0.,0.),(0.,0.,0.2)],spacegroup='I41/amd',cellpar=[tio2A_a,tio2A_a,tio2A_c,tio2A_alpha,tio2A_alpha,tio2A_alpha])


# view(tio2_bulk)
db.write(tio2_bulk, code="tio2A", note='Anatase TiO2', url='http://rruff.geo.arizona.edu/AMS/minerals/Anatase')

# for row in db.select():
#     print(row.symbols)

# row = db.get(code='tio2A')
# for key in row:
#     print('{0:22}: {1}'.format(key, row[key]))

# row = db.get_atoms(code='tio2A')
# view(row)

# db.update(db.get(code='tio2A').id,code="tio2B") 
# a = read('cells.db@name=tio2A')


