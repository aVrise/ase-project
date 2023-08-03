from ase.io import read

a = read('POSCAR')

c = a*(1,3,1)

b = a*(1,3,2)

b.positions += [10,0,0]

l = []
for atom in b:
    if atom.position[2] < 15:
        l.append(atom.index)

del b[l]

b += c

b.edit()