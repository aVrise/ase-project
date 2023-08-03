'''
use along with pos2img.py
#1 p; #2 blacklist; #3 pos2img.json; #4 POSCARs
/usr/local/opt/python@3.9/bin/python3.9 /Users/jy/Documents/work_place/ase-project/dedup.py 100000 /Users/jy/Library/CloudStorage/OneDrive-Personal/severfiles/202211/active_sites_stt/list_100077 _out/dedup/111079.json | xargs ase gui
'''

from itertools import combinations
import numpy as np
import json
import sys

def sim(dat,p = 100):
    # print(dat)
    flag0 = 0
    flag1 = 0
    flag2 = 0
    # print(ii)
    if set(dat[0].keys()) != set(dat[1].keys()):
        return False 
        # return True

    for j in dat[0].keys():
        if j in ['code','path','file']:
            continue
        if j > 20 :
            k = 1
        else:
            k = 1
        
        # 1
        # for i in set(dat[0][j].keys()) | set(dat[1][j].keys()):
        #     if i in dat[0][j].keys():
        #         t0 = dat[0][j][i]
        #     else:
        #         t0 = 0
        #     if i in dat[1][j].keys():
        #         t1 = dat[1][j][i]
        #     else:
        #         t1 = 0
        #     # if abs(t1-t2) < p:
        #     flag+=abs(t0-t1)*k

        #2 
        for kk in [0,1,2]:
            # print(j)
            count=set()
            for i in set(dat[0][j].keys()) | set(dat[1][j].keys()):
            # for i in dat[0][j].keys():
                t0=t1=n=0; 
                if i in count:
                    continue
                # print(i)
                for ii in range(i-kk,i+kk+1):
                    if ii in dat[0][j].keys():
                        t0 += dat[0][j][ii]
                        n+=1
                        count.add(ii)
                    if ii in dat[1][j].keys():
                        t1 += dat[1][j][ii]
                        n+=1
                        count.add(ii)
                    # if abs(t1-t2) < p:
                if kk == 0:
                    flag0 += abs(t0-t1)*k
                elif kk == 1:
                    flag1 += abs(t0-t1)*k
                elif kk==2 :
                    flag2 += abs(t0-t1)*k
                # flag1+=abs(t0-t1)*k*(2-kk)#/n*2

    flag=min(flag0, flag1,flag2)
    # print(flag)

    if flag < p:
        return True
    else:
        return False
# select_list = ['100046250000','100046250002']#,'100077110121']
path = '/Users/jy/Library/CloudStorage/OneDrive-Personal/severfiles/202211/active_sites_stt/'
blacklist = ['POSCAR_111078_220172','POSCAR_111077_220172','POSCAR_111079_230122','POSCAR_111078_230122','POSCAR_111077_230122','POSCAR_111047_230122','POSCAR_111046_230122','POSCAR_111045_230122','POSCAR_111079_250122','POSCAR_111079_220022','POSCAR_111028_240242','POSCAR_111047_240242','POSCAR_111077_240242','POSCAR_111078_240242','POSCAR_111079_240242','POSCAR_111028_230122',]
# with open('_out/dedup/111047-1.dat','r') as f:
#     a = int(f.readline())
#     data = [[] for x in range(100)]
#     elel = []
#     # data[amount of elements][structurs]
#     for i in range(a):
#         b = f.readline().strip().split()
#         c = [int(x) for x in b[1:]]
#         if 255 in c:
#             print(path+b[0])
#             continue
#         code = ''.join(b[0].split('_')[1:])
#         ele = code[6:10]
#         if ele not in elel:
#             elel.append(ele)
#         data[elel.index(ele)].append(dict(zip(['code','path']+c[:int(len(c)/2)],[code,path+b[0]]+c[int(len(c)/2):])))

with open(sys.argv[2],'r') as f:
    a = f.readlines()
    blacklist0 = [x.strip() for x in a]
    # print(blacklist0)

for jsonfiles in sys.argv[3:]:
    # with open('_out/dedup/111079.json', 'r') as f:
    with open(jsonfiles, 'r') as f:
        a = json.load(f)
        # for i in a:
        #     print(i)
        # exit()
        # print(a[0])
        # exit()
        # a=[]
    codelist=[]
    if 'select_list' in locals().keys():
        codelist=select_list
        select_list=[]
    data = [[] for x in range(100)]
    elel = []
    # data[amount of elements][structurs]
    for ii in a:
        if ii['file'] in blacklist0:
            #skip filted ones
            continue
        i = {}

        # ii for dict of each image/structure; jj for keys->atomic number; jk for dict of height(kj): number of pixel(kk), ji is int(jk)
        for jj, jk in ii.items():
            ji = {}
            if jj in ['file']:
                i[jj] = jk
                continue
            # for kj, kk in jk.items():         
            #     ji[int(kj)] = int(kk)
            # i[int(jj)] = ji
            for kj, kk in jk.items():
                ji[int(kj)%256] = int(kk)
            i[int(jj)%256] = ji

        b = list(i.keys())
        c = [int(x) for x in b[:-1]]
        code = ''.join(i['file'].split('_')[1:])
        i['code'] = code
        i['path'] = path+i['file']
        ele = code[6:10]       
        if i['file'] in blacklist:
            # print(i['file'])
            # print(i['path'])
            continue
        if ele not in elel:
            elel.append(ele)
        data[elel.index(ele)].append(i)
        if codelist != [] and code in codelist:
            select_list.append(i)

    # print(elel)
    # print([len(x) for x in data[:60]])
    sim90 = []
    if 'select_list' in locals().keys():
        print(select_list)
        for i in combinations(select_list,2):
            if sim(i,int(sys.argv[1])):
                sim90.append(i[x]['file'] for x in range(2))
    else:
        for i in range(len(elel)):
            if len(data[i]) == 1:
                # eliminate isolate case
                continue

            for ii in combinations(data[i],2):
                if sim(ii, int(sys.argv[1])):
                    sim90.append([ii[x]['file'] for x in range(2)])
                    # sim90.append([ii[x]['path'] for x in range(2)])
            # break

    # print(len(sim90))
    print('\n'.join([y for x in sim90 for y in x]))
        # 




