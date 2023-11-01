from ase.spacegroup import crystal
from ase.build import fcc111, add_adsorbate, bulk
from ase import Atoms
from ase.io import read, write
from ase.build import surface, molecule, sort
from ase.visualize import view
from ase.db import connect
from ase.build.surfaces_with_termination import surfaces_with_termination
from ase.io.vasp import write_vasp,read_vasp
import inspect
import numpy as np

# ads = {'nh': Atoms('NH',[(0,0,0), (0, 0, 1.0168)]), 'nh2': Atoms('NH2',[(0,0,0), (0, 0, 1.0168), (0, 1.0168, 0)]), 'n': Atoms('N'), 'h': Atoms('H'), 'o': Atoms('O'), 'oh':Atoms('OH',[(0,0,0), (0, 0, 0.9686)]),'nho':Atoms('NHO',[(0,0,0), (0, -0.719, .719), (0,.803,.803)]), 'noh':Atoms('NOH',[(0,0,0), (0, 0, .803),(0,.685,.685+.803)]),'nhoh':Atoms('NHOH',[(0,0,0), (0, -0.719, .719), (0,.803,.803), (0,.803+.685,.803-.685)]),'nh2o':Atoms('NH2O',[(0,0,0), (.415, -.415, .415), (-.415,-.415,.415), (0,.803,.803)]),'nh2oh': Atoms('NH2OH',[(0,0,0), (.415, -.415, .415), (-.415,-.415,.415), (0,.803,.803), (0,.803+.685,.803-.685)]) }
a = connect('coop.db')
# db1=connect('surs.db')
# db2=connect('mole.db')
# ads=molecule('H2O')
# a = Atoms(ads.symbols, ads.positions+[5.,5.,5.], cell=[10,10,10,90,90,90]) # build a mole within a cell
b = a.get_atoms(code='_ti_4x4')
bb = a.get_atoms(code='_ni_4x4')
# a.write(b,code='_ti_4x4', note='ti 3l1b k3x3')

# ads = Atoms('N2')
# ads=db2.get_atoms(code='_ch4')
# ads.pbc = (False, False, False)
# add_adsorbate(b,ads['NH'], 1.5, (4.9,3.19) ) # hollow

# a = db1.get_atoms(code='_110_ruo2R_600_d3_T_1x2')
# b = db1.get_atoms(code='_0ch4_0ch3h_110_tio2R_k4_400_600_d3_1x2')
# b = db1.get_atoms(code='_Ach4_110_tio2_1x2_400_600_d3')
# b = db1.get_atoms(code='_Bch4_110_tio2_1x2_k4_400_600_d3')
# b = db1.get_atoms(code='_0ch4_110_iro2R_600_d3_T_1x2')
# b = db1.get_atoms(code='_1ch3h_110_iro2R_600_d3_T_1x2')
# view(b)
# for x in b:
#     if x.symbol in ['H','C']:
#         x.position += a[46].position - b[19].position
#         cel = np.array([b.cell[0,0],b.cell[1,1],b.cell[2,2]])
#         x.position = x.position - ((x.position - cel) > 0)*cel
#         a.extend(x)
for x in ['h','n','o','noh','oh','nh','nho','nh2oh','nhoh','nh2','nh2o']:
# for x in ['nh']:
    c = b.copy()
    d=read_vasp('/Users/jy/severfiles/202104/POSCAR_'+x)
    for y in d :
        if y.symbol in ['H','N','O']:
            y.position += b[12].position - bb[12].position
            c += y
    # c.edit()
    write_vasp('../_out/PoSCAR_ti_{}'.format(x),sort(c),direct=True)


# ads.edit()
# b.edit()
# db1.write(a, code='0ch4_0ch3h_110_rio2R_k4_400_600_d3_1x2', note='0ch4 -> 1ch3 IrO2R k2x2 400 d3 1x2')
# write_vasp('POSCAR',sort(a),direct=True)
# [print(np.linalg.norm(x.position - ads[0].position)) for x in ads]

