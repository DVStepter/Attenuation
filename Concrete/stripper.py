import itertools
import os
import sys

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
