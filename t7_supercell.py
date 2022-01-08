import sys,os
from ase.constraints import FixAtoms
from ase.io import write
from ase.db import connect
import ase.build as bl
from ase.visualize import view
from ase.io.vasp import read_vasp,write_vasp
import numpy as np
from ase import Atoms

a = connect('surs.db')
ori_sur = a.get_atoms(code='_110_iro2R_600_d3_T_1x2')
super_sur = bl.sort(ori_sur*(2,3,1))
view(super_sur)