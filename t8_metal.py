from ase.build import bulk, surface, fcc100, fcc110, fcc111, hcp0001, bcc110, molecule, hcp10m10
from ase.calculators.emt import EMT
from ase.eos import calculate_eos
from ase.db import connect
from ase.io.vasp import read_vasp,write_vasp
from ase.io import write
from ase.constraints import FixAtoms
import sys, os
import numpy as np
from ase.geometry import get_duplicate_atoms 

# path = '/Users/jy/Library/CloudStorage/OneDrive-Personal/severfiles/202301/fcc_nor_gdos/pos'
# cell_parameter={'Ag':4.162, 'Au':4.164, 'Pt':3.9397, 'Pd': 3.9164, 'Cu':3.5819, 'Ni': 3.4891, 'Rh': 3.7964, 'Ir': 3.8422} #ivdw11 rpbe
# # # cell_parameter={'Ag':0, 'Au':0, 'Pt':0, 'Pd': 0, 'Cu':3.3969, 'Ni': 0, 'Rh': 0, 'Ir': 0} #ivdw12 rpbe
# ele = 'Pt'
# atoms = bulk(ele, 'hcp',a=2.494,c=4.031)#, cubic=True)# * (8,1,1)
# # atoms = bulk(ele,'fcc',a=cell_parameter[ele], cubic=True)# * (8,1,1)
# # atoms.edit()
# # slab = fcc111(ele,(1,1,6),a=cell_parameter[ele],vacuum=1.2015)#,orthogonal=True) 
# # slab = fcc111(ele,(8,1,4),a=cell_parameter[ele],vacuum=0)#,orthogonal=True) 
# slab = surface(atoms, (1,0,0),4,7.5) * (2,2,1) 
# # slab2 = hcp10m10('Co',(4,4,4),a=2.494,c=4.031,vacuum=7.5)
# slab.edit()
# # slab2.edit()
# # write_vasp('POSCAR',slab,sort=True,direct=True,wrap=True)


# for ele in cell_parameter.keys():#['Cu','Ir','Ni','Rh']:
#     atoms = bulk(ele, 'fcc',a=cell_parameter[ele], cubic=True)
#     # slab = fcc100(ele,(3,3,6),a=cell_parameter[ele],vacuum=7.5)
#     # slab = fcc110(ele,(2,3,10),a=cell_parameter[ele],vacuum=7.5)
#     # slab = fcc111(ele,(3,3,6),a=cell_parameter[ele],vacuum=7.5)
#     # slab = surface(atoms,(2,1,0),7,7.5) * (1,2,1)
#     # slab = surface(atoms,(2,1,1),7,7.5) * (1,2,1)
#     # slab = surface(atoms,(3,1,0),9,7.5) * (1,2,1)
    
#     slab221 = surface(atoms,(2,2,1),12,7.5) * (3,3,1)
#     # slab221.cell[0,:] = slab221[221].position - slab221[194].position # thickness = 7
#     # slab221.cell[1,:] = slab221[137].position - slab221[194].position # thickness = 7
#     slab221.cell[0,:] = slab221[379].position - slab221[184].position # thickness = 12
#     slab221.cell[1,:] = slab221[235].position - slab221[184].position # thickness = 12
#     slab221.wrap()
#     get_duplicate_atoms(slab221, delete=True)
#     slab221.rotate(slab221.cell[0,:], (1,0,0), rotate_cell=True)
#     slab = slab221 * (1,3,1)
    
#     # slab511 = surface(atoms,(5,1,1),14,7.5)
#     # del_list = [x.index for x in slab511 if x.scaled_position[0] > 0.49999]
#     # del slab511[del_list]
#     # slab511.cell[0,:] /= 2
#     # slab = slab511 * (1,2,1)
#     # slab.positions += 0.3*slab.cell[0,:]

#     fix = FixAtoms(indices=[x.index for x in slab if x.position[2] <= np.average(slab.positions,axis=0)[2]])
#     slab.set_constraint(fix)

#     # gcn
#     # cdlist = [ np.where((x < 3.4) * (x > 0))[0] for y,x in enumerate(slab.get_all_distances(mic=True))] 
#     # for i in slab:
#     #     if np.sum([len(cdlist[x])/12 for x in cdlist[i.index]]) == 12 :
#     #         print(i.index)

#     # slab.edit()
#     write_vasp('{:s}/POSCAR_{:s}221_sur_g'.format(path,ele.lower()),slab,sort=True,direct=True,wrap=True)
#     # exit()

# atoms = bulk('Ag', 'fcc',a=4.208, cubic=True)
# atoms = bulk('Au', 'fcc',a=4.20, cubic=True)
# atoms = bulk('Pt', 'fcc',a=3.9898, cubic=True)
# atoms = bulk('Ru', 'fcc',a=3.9898, cubic=True) # fake
# atoms = bulk('Pd', 'fcc',a=3.9796, cubic=True)
# atoms = bulk('Cu', 'fcc',a=3.6840, cubic=True) # rpbe
# atoms = bulk('Ni', 'fcc',a=3.557, cubic=True)
# atoms = bulk('Rh', 'fcc',a=3.8457, cubic=True)
# atoms = bulk('Ir', 'fcc', a=3.8843, cubic=True)
# atoms = bulk('Mo', 'bcc')
# atoms = bulk('Cu', 'fcc',a=3.6330, cubic=True) #pbe
# slab = surface(atoms,(2,2,1),8,7.5) * (3,3,1)
# slab.positions += 0.4*slab.cell[0,:]

# slab = surface(atoms,(1,0,0),3,7.5) * (2,2,1)

#special for fcc(511)
# slab511 = surface(atoms,(5,1,1),12,7.5)
# del_list = [x.index for x in slab511 if x.scaled_position[0] > 0.49999]
# del slab511[del_list]
# slab511.cell[0,:] /= 2
# slab = slab511 * (1,2,1)
# slab.positions += 0.3*slab.cell[0,:]
# 7.205913075037751, 0.0, 0.0], [3.6029565375188755, 6.240503780445133, 0.0], [0.0, 0.0, 20.88360338823072]
# slab = fcc111('Ni',(3,3,3),a=3.557,vacuum=7.5)#,orthogonal=True) 
# slab = fcc100('Ni',(1,1,4),a=3.557,vacuum=7.5,orthogonal=True) 
# slab = fcc100('Pt',(3,3,4),a=4.1618,vacuum=7.5,orthogonal=True) 
# slab = fcc111('Cu',(3,3,4),a=3.3969,vacuum=7.5,orthogonal=False)
# slab = fcc111('Ag',(4,4,3),a=4.208,vacuum=7.5,orthogonal=True)
# slab = fcc111('Au',(4,4,3),a=4.20,vacuum=7.5,orthogonal=True) 
# slab = fcc111('Pt',(1,2,3),a=3.9898,vacuum=7.5,orthogonal=True)
# slab = fcc111('Pd',(4,4,3),a=3.9796,vacuum=7.5,orthogonal=True)
# slab = bcc110('V',(2,2,3),a=3.001,vacuum=7.5,orthogonal=True)
# slab = hcp0001('Ti',(2,2,3),a=2.9225, c=4.6329, vacuum=7.5,orthogonal=True) 
# slab = hcp0001('Ti',(2,2,3),a=2.9446836397465557, c=4.6715667106969461, vacuum=7.5,orthogonal=True)

# slab = fcc111('Ni',(3,3,3),a=3.5517,vacuum=7.5,orthogonal=True) 
# slab = fcc111('Cu',(3,3,3),a=3.6769,vacuum=7.5)
# slab = fcc111('Ag',(3,3,3),a=4.2072,vacuum=7.5)
# slab = fcc111('Au',(3,3,3),a=4.1971,vacuum=7.5) 
# slab = fcc111('Pt',(3,3,3),a=3.9899,vacuum=7.5)
# slab = fcc111('Pd',(3,3,3),a=3.9819,vacuum=7.5)
# slab = fcc111('Rh',(3,3,3),a=3.8457,vacuum=7.5)
# slab = fcc111('Ir',(3,3,3),a=3.8844,vacuum=7.5)

# slab = fcc100('Ni',(3,3,3),a=3.5517,vacuum=7.5) 
# slab = fcc100('Cu',(3,3,3),a=3.6769,vacuum=7.5)
# slab = fcc100('Ag',(3,3,3),a=4.2072,vacuum=7.5)
# slab = fcc100('Au',(3,3,3),a=4.1971,vacuum=7.5) 
# slab = fcc100('Pt',(2,2,3),a=3.9899,vacuum=7.5)
# slab = fcc100('Pd',(3,3,3),a=3.9819,vacuum=7.5)
# slab = fcc100('Rh',(3,3,3),a=3.8457,vacuum=7.5)
# slab = fcc100('Ir',(3,3,3),a=3.8844,vacuum=7.5)

# 

# fix = FixAtoms(indices=[x.index for x in slab if x.position[2] < 10])
# slab.set_constraint(fix)

# print(slab.cell)
# atoms = molecule('CO')
# slab.edit()
# atoms.edit()

# write('ni311.xyz',slab)
# write('Ni111.cif',slab)
# write_vasp('POSCAR',slab,sort=True,direct=True,wrap=True)
# write_vasp('POSCAR',atoms,sort=True,direct=True)

# for i in sys.argv[1:]:
#     a = read_vasp(i)
#     write_vasp(i,a,sort=True)#,direct=True)

ref = read_vasp('POSCAR')
write_vasp('POSCAR1',ref,sort=True,direct=True,wrap=True)
# b = read_vasp("/Users/jy/severfiles/202105/CONTCAR")
# for _1 in b:
#     if _1.symbol != 'Cu':
#         _1.position = _1.position * np.array([ref.cell[0,0],ref.cell[1,1],ref.cell[2,2]]) / np.array([b.cell[0,0],b.cell[1,1],b.cell[2,2]])
#         # _1.position[0] = 4.455
#         # _1.position[1] = 4.289
#         ref += _1
# ref.edit()
# write_vasp('/Users/jy/severfiles/202106/POSCAR_ch4-mno2_spins',ref,sort=True,direct=True)

# ref = read_vasp('POSCAR')
# for _ in sys.argv[1:]:
#     ref_1 = ref.copy()
#     b = read_vasp(_)
#     # sb=_[39:41]
# #     # if a[14:] in ['oh', 'o', 'n', 'h', 'noh', 'nh']:
# #     # if a[14:] in [ 'nho', 'nh2', 'nh2o', 'nhoh']:
# #     # if a[14:] == 'oh':
# #         # pos1 = b[b.get_chemical_symbols().index('N')].position
# #         # dd = pos - pos1 * np.array([ref.cell[0,0],ref.cell[1,1],ref.cell[2,2]]) / np.array([b.cell[0,0],b.cell[1,1],b.cell[2,2]])
#     for _1 in b:
#         if _1.symbol != 'Ni':
#             # _1.position = _1.position * np.array([ref.cell[0,0],ref.cell[1,1],ref.cell[2,2]]) / np.array([b.cell[0,0],b.cell[1,1],b.cell[2,2]])
#             _1.position = _1.position * np.array([ref.cell[0,0],ref.cell[1,1],ref.cell[2,2]]) / np.array([b.cell[0,0]/4*3,b.cell[1,1]/4*3,b.cell[2,2]])
#             # _1.position[0] = 4.455
#             # _1.position[1] = 4.289
#             ref_1 += _1
#     # ref_1.edit()
#     # write_vasp('/Users/jy/severfiles/202205/111_3x3/POSCAR_Ni111_'+_.split('/')[-1][14:],ref_1,sort=True,direct=True)
#     write_vasp('/Users/jy/severfiles/202205/100_3x3/POSCAR_'+'Rh'+'100_'+_[42:],ref_1,sort=True,direct=True)
                                    
# write_vasp('POSCAR1',ref,sort=True,direct=True)
# with open("/Users/jy/severfiles/202106/list",'r') as f1:
#     for _ in range(24):
#         a = f1.readline().strip()
#         b = read_vasp("/Users/jy/severfiles/202106/"+a)
#         write_vasp('/Users/jy/severfiles/202106/ni210/'+a,b,sort=True,direct=True)

# for _ in sys.argv[1:]:
#     b = read_vasp(_)
#     _2 = []
#     for _1 in b:
#         if _1.symbol == 'H':
#             _2.append(_1.index)
#     del b[_2]
#     # b.edit()
#     # print(_.split('/')[-1][:13])
#     name = {'_noh':'no_0','nhoh':'no_1','nh2o':'no_2'}
#     # print('/Users/jy/severfiles/202205/'+_.split('/')[-1][:13]+name[_.split('/')[-1][-4:]])
#     write_vasp('/Users/jy/severfiles/202205/'+_.split('/')[-1][:13]+name[_.split('/')[-1][-4:]],b,sort=True,direct=True)
    # write_vasp(_+'_s',b,sort=True, direct=True)

# with open("/Users/jy/severfiles/202111/list",'r') as f1:
#     for _ in range(9):
#         a = f1.readline().strip()
#         b = read_vasp("/Users/jy/severfiles/202111/"+a)
#         write_vasp('/Users/jy/severfiles/202111/'+a+'s',b,sort=True,direct=True)

# for i in sys.argv[1:]:
#     write(i[7:]+'.xyz',read_vasp(i))

# a_vector={'ir':[99,405],'ti':[392,291],'ru':[471,144],'rh':[460,53],'os':[431,79]}
# path = '/Users/jy/Library/CloudStorage/OneDrive-Personal/severfiles/stt/ch4_rutile110/'
# for i in ['ir','ti','ru','rh','os']:
#     # ref = read_vasp(path+"CONTCAR_"+i+"_ch3h") ; ref_vector={'ir':[31,196],'ti':[134,7],'ru':[147,100],'rh':[177,7],'os':[176,100]}
#     ref = read_vasp(path+"CONTCAR_"+i+"_tran") ; ref_vector={'ir':[31,196],'ti':[156,100],'ru':[134,36],'rh':[156,38],'os':[156,36]}

#     a = read_vasp(path+"CONTCAR_"+i+"o2_ch4_big")
#     v_ref = ref[ref_vector[i][1]].position - ref[ref_vector[i][0]].position
#     v_a = a[a_vector[i][1]].position - a[a_vector[i][0]].position

#     rot_cos = v_a.dot(v_ref)/np.linalg.norm(v_a)/np.linalg.norm(v_ref)
#     rot_sin = np.sqrt(1 - rot_cos**2)
#     m_rotation = np.array([[rot_cos,rot_sin,0],[-rot_sin,rot_cos,0],[0,0,1]])
#     ref.positions = ref.positions.dot(m_rotation)
#     # ref.rotate(v_ref,v_a)
#     # ref.edit()
#     dd = ref[ref_vector[i][0]].position - a[a_vector[i][0]].position

#     # print(a[:5].positions)

#     # ref.edit()
#     for ii in range(5):
#         a[ii].position = ref[ii].position - dd
    
#     a[a_vector[i][1]].position = ref[ref_vector[i][1]].position - dd
#     # a[:5].positions = ref[:5].positions - dd
#     # print(np.hstack([a[:5].positions,ref[:5].positions - dd]))
#     # a.edit()
    # write_vasp('/Users/jy/Library/CloudStorage/OneDrive-Personal/severfiles/202106/CONTCAR_'+i+'_tran_big',a,sort=True,direct=True)

# # cell_parameter={'Ag':4.162, 'Au':4.164, 'Pt':3.9397, 'Pd': 3.9164, 'Cu':3.5819, 'Ni': 3.4891, 'Rh': 3.7964, 'Ir': 3.8422} #ivdw11 rpbe
# # # cell_parameter_ori={'Ag':4.208, 'Au':4.20, 'Pt':3.9898, 'Pd': 3.9796, 'Cu':3.6840, 'Ni': 3.557, 'Rh': 3.8458, 'Ir': 3.8843}
# path = '/Users/jy/Library/CloudStorage/OneDrive-Personal/severfiles/202301/fcc_nor_210/'
# path0 = '/Users/jy/Library/CloudStorage/OneDrive-Personal/severfiles/202107/ni210_pos/'
# # ref0 = read_vasp(path+'CONTCAR_ir221_sur_0')

# # for i in sys.argv[1:]:
# for i in [
# 'POSCAR_Ni210_Jul6_h_0', 'POSCAR_Ni210_Jul6_h_1', 'POSCAR_Ni210_Jul6_h_2', 'POSCAR_Ni210_Jul6_n_0', 'POSCAR_Ni210_Jul6_n_1', 'POSCAR_Ni210_Jul6_n_2', 'POSCAR_Ni210_Jul6_nh2_0', 'POSCAR_Ni210_Jul6_nh2_1', 'POSCAR_Ni210_Jul6_nh2o_0', 'POSCAR_Ni210_Jul6_nh2o_1', 'POSCAR_Ni210_Jul6_nh2o_2', 'POSCAR_Ni210_Jul6_nh2oh_0', 'POSCAR_Ni210_Jul6_nh2oh_1', 'POSCAR_Ni210_Jul6_nh_0', 'POSCAR_Ni210_Jul6_nh_1', 'POSCAR_Ni210_Jul6_nh_2', 'POSCAR_Ni210_Jul6_nho_0', 'POSCAR_Ni210_Jul6_nho_1', 'POSCAR_Ni210_Jul6_nhoh_0', 'POSCAR_Ni210_Jul6_nhoh_1', 'POSCAR_Ni210_Jul6_noh_1', 'POSCAR_Ni210_Jul6_noh_2', 'POSCAR_Ni210_Jul6_o_0', 'POSCAR_Ni210_Jul6_o_1', 'POSCAR_Ni210_Jul6_oh_0', 'POSCAR_Ni210_Jul6_oh_1',
# ]:
#     if 'sur' in i:
#         continue
# # #     j = i[7:12]
    
#     ref = read_vasp(path0+i)
#     i = i[:12] + i[17:]
#     ele = i[7:9].lower()
#     facet = path[-4:-1]
#     ref0 = read_vasp(path0+'POSCAR_Ni210_Jul6_h_0')
#     #     # ref = read_vasp('POSCAR_t')


#     #         sur = read_vasp(path+"CONTCAR_{:s}221_sur_0".format(i_))
#     #         cell_parameter_changed = ref.cell * cell_parameter[i_.capitalize()] / cell_parameter['Ir']
#     #         ref.set_cell(cell_parameter_changed,scale_atoms=True)
#     #         # dd = sur[29].position - ref0[29].position
#     #         for ij in ref:
#     #             if ij.number < 20:
#     #                 sur += ij
#     #         write_vasp(path+"POSCAR_{:s}{:s}".format(i_,i[9:]),sur,sort=True,direct=True)


#         # for 110 only clockwise 90˚
#         # ref.rotate(-90,'z',rotate_cell=True)
#         # ref0.rotate(-90,'z',rotate_cell=True)
        
#         # ref.edit()
#         # exit()
#     for i_ in ['ni', 'rh', 'pd', 'ag', 'pt', 'au', 'cu', 'ir']:

#         sur = read_vasp(path+'CONTCAR_{:s}_sur_0'.format(i_+facet))
#         # sur = read_vasp(path+'CONTCAR_{:s}_sur_0'.format(ele+facet))
#         for ij in ref.copy():
#             if ij.number < 20:
#                 ij.position += sur[31].position - ref0[24].position
#                 sur += ij
#                 # dd = (ij.position - [3.959, 3.558, 11.245]) #/ cell_parameter['Ni'] * cell_parameter[i_.capitalize()]
#                 # ij.position += sur[31].position + dd
#                 # sur += ij 
#         # sur.positions +=  0.3*sur.cell[0,:]
#         write_vasp(path+'{:s}{:s}{:s}'.format(i[:7],i_,i[9:].lower()),sur,sort=True,direct=True)
#         # write_vasp(path+'{:s}{:s}'.format(i[:7],i[7:].lower()),sur,sort=True,direct=True,wrap=True)

#     # sur = ref.copy()
#     # # j = i[7:9].capitalize()
#     # j = i.capitalize()
#     # cell_parameter_changed = sur.cell * cell_parameter[j] / cell_parameter['Ir']
#     # sur.set_cell(cell_parameter_changed,scale_atoms=True)
#     # for ii in sur:
#     #     ii.symbol = j
#     # write_vasp(path+'POSCAR_'+i+'221_sur_0',sur,sort=True,direct=True)






# path = '/Users/jy/Library/CloudStorage/OneDrive-Personal/severfiles/202301/fcc_nor_210/pos'
# path = '/Users/jy/Library/CloudStorage/OneDrive-Personal/severfiles/202305/fespin'
# path = '/Users/jy/Library/CloudStorage/OneDrive-Personal/severfiles/202305/cof_fespin'

# ref = read_vasp(path+'/POSCAR')#_cospin_cooh_0')
# b = ref[-4:]
# ref.positions[:,2] = 5
# for i in cell_parameter.keys():
# for i in ['co','fe','ni']:
#     for j in range(1,3):
#         a = read_vasp('{:s}/CONTCAR_{:s}spin_sur_{:d}'.format(path,i,j))
#         a += b
#         write_vasp('{:s}/POSCAR_{:s}spin_cooh_{:d}'.format(path,i.lower(),j),a, direct=True)
# write_vasp('{:s}/POSCAR0'.format(path),ref, direct=True, sort= True)