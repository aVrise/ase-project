# from ase.build import bulk, surface, fcc100, fcc110, fcc111, hcp0001, bcc110, molecule
# from ase.db import connect
# from ase.io.vasp import read_vasp,write_vasp
# from ase.io import write
# from ase.constraints import FixAtoms
# import sys, os
# import numpy as np


# 
from ase.build import bulk
bulk_Pt = bulk('Pt', 'fcc', cubic=True)
# bulk_Pt.edit()

#
from ase.build import fcc100, fcc110, fcc111
# surface_Pt_111 = fcc111('Pt',(3,3,5),a=3.91789,vacuum=7.5)
surface_Pt_100 = fcc100('Pt',(3,3,5),a=3.91789,vacuum=7.5)
# surface_Pt_110 = fcc110('Pt',(2,3,5),a=3.91789,vacuum=7.5)
# surface_Pt_111.edit()
surface_Pt_100.edit()
# surface_Pt_110.edit()