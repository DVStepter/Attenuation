import itertools
import os
import sys
import numpy as np

filter_list = ['PAIR','PHOT','BREM','RAYL','IONI','INEL','CAPT','DECA','ANNI','ESCP','SE','ID','TI','ED','EC','NS','PM','EN','TE','TS']

with open(sys.argv[1],'r') as input: #filters out unwanted interactions
    with open('New.sim','w') as output:
        for line in input:
            if all(nb not in line for nb in filter_list):
                output.write(line)

os.remove(sys.argv[1])

lines = [] #Reverses file to be read from bottom to top
with open('New.sim', 'r') as f:
    lines = f.readlines()
with open('New_Rev.sim', 'w') as f:
    for line in reversed(lines):
        f.write(line)

os.remove('New.sim')

#Creates function to remove extra spaces in sim file
def cleanlines(line):
    remove = ['  ', ' ']
    for r in remove:
        clean = line.replace(r, '')
    split = clean.split(';')
    return split

#Creates empty list for x, y, z, and energy value of hits
xlist = []
ylist = []
zlist = []
elist = []
lastx = []
lasty = []
lastz = []

data = open('New_Rev.sim', 'r')
for l in data:
    line = cleanlines(l.strip('\n'))
    if line[0][2:6] == 'BLAK' and line[1] == '1':  #len(line) >= 1 and
        elist.append(np.float32(line[14]))
        xlist.append(np.float32(line[4]))
        ylist.append(np.float32(line[5]))
        zlist.append(np.float32(line[6]))
        line2 = cleanlines(next(data).strip('\n'))
        lastx.append(np.float32(line2[4]))
        lasty.append(np.float32(line2[5]))
        lastz.append(np.float32(line2[6]))
data.close()

os.remove('New_Rev.sim')

#Converting to cylindrical coordinates (r,phi,z)
#Generates phi -180 to 180 degrees
phi = np.arctan2(ylist,xlist)*180/np.pi

Tot = np.array(list(zip(xlist,ylist,zlist,elist,lastx,lasty,lastz,phi)))

np.save('total.npy', Tot)
