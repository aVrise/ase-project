from ase import Atoms
from ase.visualize import view

nh3 = Atoms('NH3',[(5.0,5.0,5.1),(5.0,5.9,4.7),(5.8,4.5,4.7),(4.2,4.5,4.7)])
# view(nh3)

# print('atomic numbers:',nh3.numbers)
# print('atomic numbers:',nh3.get_atomic_numbers())
# print('chemical formula:',nh3.symbols)
# print('chemical formula:',nh3.get_chemical_formula())

# for id,atom in enumerate(nh3):
#     print(id)
#     print(atom.index,atom.symbol,atom.number)
#     print(nh3[id].index,nh3[id].symbol,nh3[id].number)
#     print(atom.position)

# nh3_0=nh3.copy()
# for atom in nh3_0:
#     if atom.symbol == 'N':
#         atom.symbol = 'C'
#     else :
#         if atom.position[1] > 5:
#             id = atom.index
#         else:
#             atom.position += 0.1
# del nh3_0[id]

# for id,atom in enumerate(nh3_0):
#     print(atom.index,atom.symbol,atom.number)
#     print(atom.position)

# nh3_0.edit()

from ase.build import molecule, bulk, surface

co = molecule('CO')
# co.edit()
# print(co.positions)

bulk_cu = bulk('Cu','fcc',a=3.6840)#,cubic=True)
# bulk_cu.edit()

surface_cu = surface(bulk_cu,(1,1,1),3,7.5) * (2,2,1)
# surface_cu.edit()

from ase.build import add_adsorbate

add_adsorbate(surface_cu,co,3,(4.9,3.19))
# surface_cu.edit()

# from ase.constraints import FixAtoms

# fix = FixAtoms(indices=[x.index for x in surface_cu if x.position[2] < 9])
# surface_cu.set_constraint(fix)
# # surface_cu.edit()

# from ase.io.vasp import read_vasp,write_vasp

# # surface1 = read_vasp('POSCAR')
# write_vasp('POSCAR',surface_cu,sort=True,direct=True)