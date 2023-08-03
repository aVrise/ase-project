from ase.db import connect
from ase.spacegroup import crystal
from ase.visualize import view
from ase.io.vasp import write_vasp,read_vasp
from ase.build import sort

# build a connection to the datebase
# db = connect('ucells.db') 

# unit cell parameters
# cell=[4.4839, 4.5385, 3.1360, 90, 90, 90] # TiO2 for example
cell=[8.44, 8.44, 8.44, 90, 90, 90] # TiO2 for example
# ca=4.4862
# cc=3.0884
# cell=[ca, ca, cc, 90, 90, 90]
x = read_vasp('POSCAR')

# build a unit cell
# x = crystal(['Rh','O'],[(0.,0.,0.),(0.304,0.304,0)],spacegroup='P42/mnm',cellpar=cell)
# x = crystal(['Ti','O'],[(0.,0.,0.),(0.,0.,0.2)],spacegroup='I41/amd',cellpar=cell)
# x = crystal(['Pt','O'],[(0.,0.,0.),(0.2670,0.35,0)],spacegroup='Pnnm',cellpar=cell)
x = crystal(['Fe','Fe','O'],[(0.5,0.,0.5),(7/8,7/8,5/8),(0.13135,0.86865,0.13135)],spacegroup='Fd-3m',cellpar=cell)

#modify cell parameter
# x = db.get_atoms(code='ruo2R')
# x[0].symbol = 'Cr'
# print(x.cell)
# x.cell=[x.cell[0][0],x.cell[0][0],x.cell[2][2],90,90,90]
# print(x.cell)


# view(x*(4,4,2))
# a = x*(4,4,2)
# write_vasp("POSCAR_la2o3_4_4_2",a,sort=True)

# db.write(x, code="rho2R", note='Rutile RhO2 cell', url='https://www.sciencedirect.com/science/article/pii/0038109868900197')
# db.write(x, code="ruo2R_600_d3_T_u", note='Rutile RuO2 cell opt 600eV PBE-D3 Ru_pv Ueff=2 eV', url='')
# db.update(db.get(code='BETApto2R_600_d3_T').id, x) 

# for row in db.select():
#     print(row.symbols)

# row = db.get(code='tio2R_600_d3')
# for key in row:
#     print('{0:22}: {1}'.format(key, row[key]))

# row = db.get_atoms(code='tio2A')
# view(row)

# print(db.get(code='tio2R_600_d3').id)

# a = read('cells.db@name=tio2A')
write_vasp('POSCAR',sort(x),direct=True)
x.edit()

