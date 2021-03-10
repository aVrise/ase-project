#!/usr/bin/env python
'''
A Python-based VASP input files generator from ase database

usage:
    po.py <input>

    <input>:    an input file contains essential contents shown as following.

                # Comments
                tio2R # the code of structures
                cel # system: cell optimizing (cel), surface relaxation (sur), molecule (mol)
                opt # optimizing(opt), single point(sp), density of state(dos)
                111 # Kpoints
                0.2 # Fix atoms under this z value. When this number is less than 1, a fraction z value will be applied. When this number is no more than 0, no atom will be fixed.
                ISTART=1 # specified parameter below
                LDAU=Ti:3.5;O:0 # sequence is not required
                LWAVE # or just specified the name to get the default value. (not available for LDAU)

requirements:
    modules:                    ase 3.21.1
    environment variable:       ASEDBCELL for the path of cell ase database
                                ASEDBMOL for the path of cell ase database
                                ASEDBSUR for the path of surface ase database
                                ASEDBOSUR for the path of optimized surface ase database
                                VASPPP for directory of vasp pseudopotential
                                VASPSCR for the path of vasp job script

'''

import os
import sys

import ase.build as bl
from ase.constraints import FixAtoms
from ase.db import connect
from ase.io.vasp import write_vasp




def readata(a, b, c):
    global par
    # Need to set the ENVIRONMENT VARIABLES to locate the corresponding ase database
    x = {"cel": 'ASEDBCELL', '_sur': 'ASEDBOSUR', 'sur': 'ASEDBSUR', "mol": 'ASEDBMOL'}
    y = {'celopt': ['ENCUT=600', 'ISIF=3' ], 'sursp': ['LCHARG=T','LWAVE=T','NSW=0','IBRION=-1', 'NELM=200']}
    if b+c in y.keys():
        par = par[:5] + y[b+c] + par[5:] 
    return connect(os.getenv(x[b])).get_atoms(code=a)


def write_inc(a, b):

    def incar(a, b, c):

        def ldau(a, b, c, d):
            x = {'s':-1,'p':-1,'d':2,'f':3,'z':-1}
            y={}
            ldaul,ldauu,ldauj=[],[],[]
            b = [[j for j in i.strip().split(':')] for i in b.strip().split(';')]
            for i in b:
                y[i[0]]=i[1]
            for i in c:
                ldaul.append(str(x[d[i]]))
                ldauu.append(str(y[i]))
                ldauj.append('0')
            a['LDAU']=[11,1,'T']
            a['LDAUTYPE']=[11,1,2]
            a['LDAUL']=[11,1,' '.join(ldaul)]
            a['LDAUU']=[11,1,' '.join(ldauu)]
            a['LDAUJ']=[11,1,' '.join(ldauj)]
            return a

        def checkinc(b, c, e):
            # return default incar parameters b: complete incar parameter; c: element outmost orbital; e: contained elements
            def alert(alert1,alert2):
                print("The INCAR parameter value "+alert1+" was changed to "+str(alert2)+".")
            x = [2 for i in e if i in [ 'B', 'C', 'N', 'O', 'F']]
            y = {'s':0,'p':1,'d':2,'f':3,'z':0}
            e = [y[c[i]] for i in e]
            # check LMAXMIX
            if max(e) > 2 or 'LDAU' in b.keys():
                if b['LMAXMIX'][1] != 1 or b['LMAXMIX'][2] != 2*max(e):
                    b['LMAXMIX'][1] = 1
                    b['LMAXMIX'][2] = 2*max(e)
                    alert('LMAXMIX', 2*max(e))
            # check LASPH
            if max(e) > 2 or 2 in x or 'LDAU' in b.keys() or (b['LHFCALC'][1] == 1 and 'T' in b['LHFCALC'][2]):
                if b['LASPH'][1] != 1 or b['LASPH'][2] != 'T':
                    b['LASPH'][1] = 1
                    b['LASPH'][2] = 'T'
                    alert('LASPH', 'T')
            return b

        # "PARAMETER": [label, default out, default value]
        x = {"SYSTEM": [0, 1, b], "NWRITE": [1, 0, 2],  "PREC": [1, 1, "Normal"], "ISTART": [1, 1, 0],    "ICHARG": [1, 1, 2],   "ISPIN": [1, 1, 2],   'LNONCOLLINEAR': [1, 0, 'F'], 'LSORBIT': [1, 0, 'F'],  'INIWAV': [1, 0, 1],    'LASPH': [1, 1, 'F'],   'METAGGA': [1, 0, 'F'],    'ENCUT': [2, 1, 400],   'ENINI': [2, 0, 400.0],  'ENAUG': [2, 0, 605.4],  'NELM': [2, 0, 100],   'NELMIN': [2, 0, 2],  'NELMDL': [2, 0, -5],   'EDIFF': [2, 1, 0.1E-03],    'LREAL': [2, 1, 'A'],  'NLSPLINE': [2, 0, 'F'],   'LCOMPAT': [2, 0, 'F'], 'GGA_COMPAT': [2, 0, 'T'],  'LMAXPAW': [2, 0, -100],    'LMAXMIX': [2, 0, 2],    'VOSKOWN': [2, 0, 0],   'ROPT': [2, 0, -0.00050],    'EDIFFG': [3, 1, -.3E-01],    'NSW': [3, 1, 300],    'NBLOCK': [3, 0, 1],  'KBLOCK': [3, 0, 1000],    'IBRION': [3, 1, 2],   'NFREE': [3, 0, 1],    'ISIF': [3, 1, 2], 'IWAVPR': [3, 0, 11],   'ISYM': [3, 1, 0],  'LCORR': [3, 0, 'T'],    'POTIM': [3, 1, 0.5],   'TEIN': [3, 0, 0.0], 'TEBEG': [3, 0, 0.0], 'TEEND': [3, 0, 0.0], 'SMASS': [3, 0, -3.00], 'SCALEE': [3, 0, 1.0000], 'NPACO': [3, 0, 256], 'PSTRESS': [3, 0, 'pullay'], 'POMASS': [3, 0, 16.00], 'ZVAL': [3, 0, 6.00], 'RWIGS': [3, 0, -1.00], 'VCA': [3, 0, 1.00], 'NELECT': [3, 0, 1152.0000], 'NUPDOWN': [3, 0, 'fix'], 'EMIN': [4, 0, 10.00], 'EMAX': [4, 0, -10.00],
            'EFERMI': [4, 0, 0.00], 'ISMEAR': [4, 1, 0], 'SIGMA': [4, 0, 0.05], 'ALGO': [5, 1, 'Fast'], 'IALGO': [5, 0, 68], 'LDIAG': [5, 0, 'T'], 'LSUBROT': [5, 0, 'F'], 'TURBO': [5, 0, 0], 'IRESTART': [5, 0, 0], 'NREBOOT': [5, 0, 0], 'NMIN': [5, 0, 0], 'EREF': [5, 0, 0.00], 'IMIX': [5, 0, 4], 'AMIX': [5, 1, 0.20], 'BMIX': [5, 1, 0.0001], 'AMIX_MAG': [5, 1, 0.8], 'BMIX_MAG': [5, 1, 0.0001], 'AMIN': [5, 0, 0.10], 'WC': [5, 0, 100.], 'INIMIX': [5, 0, 1], 'MIXPRE': [5, 0, 1], 'MAXMIX': [5, 0, -45], 'WEIMIN': [5, 0, 0.0010], 'EBREAK': [5, 0, 0.31E-07], 'DEPER': [5, 0, 0.30], 'TIME': [5, 0, 0.40], 'LWAVE': [6, 1, 'F'], 'LCHARG': [6, 1, 'F'], 'LVTOT': [6, 0, 'F'], 'LVHAR': [6, 0, 'F'], 'LELF': [6, 0, 'F'], 'LORBIT': [6, 0, 0], 'LMONO': [7, 0, 'F'], 'LDIPOL': [7, 0, 'F'], 'IDIPOL': [7, 0, 0], 'EPSILON': [7, 0, 1.00], 'GGA': [8, 0, '--'], 'LEXCH': [8, 0, 8], 'LHFCALC': [8, 0, 'F'], 'LHFONE': [8, 0, 'F'], 'AEXX': [8, 0, 0.0000], 'LEPSILON': [9, 0, 'F'], 'LRPA': [9, 0, 'F'], 'LNABLA': [9, 0, 'F'], 'LVEL': [9, 0, 'F'], 'LINTERFAST': [9, 0, 'F'], 'KINTER': [9, 0, 0], 'CSHIFT': [9, 0, 0.1], 'OMEGAMAX': [9, 0, -1.0], 'DEG_THRESHOLD': [9, 0, 0.002], 'RTIME': [9, 0, 0.100], 'ORBITALMAG': [10, 0, 'switch'], 'LCHIMAG': [10, 0, 'F'], 'DQ': [10, 0, 0.001000], 'NPAR': [11, 1, 4], 'IVDW': [11, 0, 0]}
        y = {'H':'s','He':'z','Li':'s','Be':'s','B':'p','C':'p','N':'p','O':'p','F':'p','Ne':'z','Na':'s','Mg':'s','Al':'p','Si':'p','P':'p','S':'p','Cl':'p','Ar':'z','K':'s','Ca':'s','Sc':'d','Ti':'d','V':'d','Cr':'d','Mn':'d','Fe':'d','Co':'d','Ni':'d','Cu':'d','Zn':'d','Ga':'p','Ge':'p','As':'p','Se':'p','Br':'p','Kr':'z','Rb':'s','Sr':'s','Y':'d','Zr':'d','Nb':'d','Mo':'d','Tc':'d','Ru':'d','Rh':'d','Pd':'d','Ag':'d','Cd':'d','In':'p','Sn':'p','Sb':'p','Te':'p','I':'p','Xe':'z','Cs':'s','Ba':'s','La':'d','Ce':'f','Pr':'f','Nd':'f','Pm':'f','Sm':'f','Eu':'f','Gd':'f','Tb':'f','Dy':'f','Ho':'f','Er':'f','Tm':'f','Yb':'f','Lu':'d','Hf':'d','Ta':'d','W':'d','Re':'d','Os':'d','Ir':'d','Pt':'d','Au':'d','Hg':'d','Tl':'p','Pb':'p','Bi':'p','Po':'p','At':'p','Rn':'z','Fr':'s','Ra':'d','Ac':'d','Th':'f','Pa':'f','U':'f','Np':'f','Pu':'f','Am':'f','Cm':'f','Bk':'f','Cf':'f','Es':'f','Fm':'f','Md':'f','No':'f','Lr':'d','Rf':'d','Db':'d','Sg':'d','Bh':'d','Hs':'d','Mt':'d'}
        for i in a:
            # update parameters
            if '=' in i:
                j = i.split('=')
                if j[0] in x.keys():
                    x[j[0]][1] = 1
                    x[j[0]][2] = j[1]
                elif j[0] == 'LDAU':
                    x = ldau(x,j[1], c, y)
                else:
                    x[j[0]] = [11, 1, j[1]]
            elif i in x.keys():
                x[i][1] = 1
            else:
                print('Wrong INCAR PARAMETER!!')
                exit()
        x = checkinc(x, y, c)
        y = []
        for i in x.keys():
            # construct a list containing all parameters
            if x[i][1] == 1:
                y.append([x[i][0], i, x[i][2]])
        return sorted(y)

    label = ["# Comments", "# Startparameter for this run", "# Electrionic Relaxation 1", " #Ionic Relaxation", "# DOS Related Values",
             "# Electronic Relaxation 2", "# Write Flags", "# Diole corrections", "# Exchange correlation treatment", "# Linear response parameters", "# Orbital Magentization Related", "# Others"]
    x = incar(a[5:], a[0], b)
    with open('INCAR', 'w') as y:
        i = -1
        for j in x:
            if j[0] != i:
                y.write(label[j[0]]+'\n')
                i = j[0]
            y.write(j[1]+' = '+str(j[2])+'\n')


def write_kpo(x):
    with open("KPOINTS", 'w') as a:
        a.write("Comments\n0\nG\n"+x[0]+" "+x[1]+" "+x[2]+"\n"+"0 0 0\n")
        if int(x[0])*int(x[1])*int(x[2]) == 1:
            return 0  # gamma
        else:
            return 1  # std


def write_pos(a, b, c):
    if a in ['cel', 'mol']:
        write_vasp('POSCAR', b, direct=True)
    else:
        stct.set_constraint(FixAtoms(indices=[x.index for x in stct if x.position[2] < max(
            c, 0)/(c-1+1e-6)*(max(c-1+1e-6, 0)+b.cell[2][2]*min(c-1+1e-6, 0))]))
        write_vasp('POSCAR', b, direct=True)


def write_pot(a):
    x = []
    ele = ""
    for i in a:
        if ele == i:
            continue
        else:
            ele = i
            x.append(ele)
            os.system("cat $VASPPP/"+ele+"/POTCAR >> POTCAR")
    return x


def write_scr(a, b, c):
    os.system("sed 's/CODENAME/"+b+"/' $VASPSCR > " + c)
    if a == 0:
        os.system('sed -i "s/vasp_std/vasp_gam/" '+c)


scr_name = 'zlauncher'
os.system('rm -f INCAR POSCAR POTCAR KPOINTS '+scr_name)
os.system('echo;echo;')
with open(sys.argv[1], "r") as ip:
    par = [x for y in ip.readlines() if y[0][0] != "#" for x in y.strip().split()[
        :2] if x[0] != "#" and x != '']
# print(par)
stct = bl.sort(readata(par[0], par[1], par[2]))
write_pos(par[1], stct, float(par[4]))
write_inc(par, write_pot(stct.get_chemical_symbols()))
write_scr(write_kpo(par[3]), par[0], scr_name)
os.system('head POSCAR; grep HF POTCAR;echo;echo;')
