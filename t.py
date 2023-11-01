from ase.build import bulk, surface, fcc100, fcc110, fcc111, hcp0001, bcc110, molecule
from ase.calculators.emt import EMT
from ase.eos import calculate_eos
from ase.db import connect
from ase.io.vasp import read_vasp,write_vasp
from ase.io import write
from ase.constraints import FixAtoms
import sys, os
import numpy as np

# a=read_vasp('POSCAR2')
# a.cell=np.array([a[18].position - a[13].position, a[14].position - a[13].position,a.cell[2,:]]).reshape([3,3])
# a.positions -= a[13].position*(1,1,0) #- 0.5*a.cell[0,:]
# del a[[13,14,17]]
# a*=(1,3,1)
# a.edit()

# fix = FixAtoms(indices=[x.index for x in a if x.position[2] < 9.4])
# a.set_constraint(fix)

# write_vasp('POSCAR_t',a,sort=True,direct=True,wrap=True)


for i in sys.argv[1:]:
    a = read_vasp(i)
    for j in a:
        if j.symbol == 'H':
            del a[j.index]
            break

    write_vasp(i, a, direct=True)