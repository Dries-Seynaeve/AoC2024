import numpy as np
from  functools import cache

with open("input.txt") as f:
    lines = [line.strip() for line in f.readlines()]

readKeys = True
keys = []
paterns = []
for line in lines:
    if line.__eq__(""):
        readKeys = False
        continue
    if readKeys:
        keys = [key.strip() for key in line.split(",")]
    else:
        paterns.append(line)

def solve(key, paterns):
    return sum(1 if can_be_made(patern) else 0 for patern in paterns)

def solve2(key, paterns):
    return sum(can_be_made(patern) for patern in paterns)

@cache
def can_be_made(patern, index=0):
    if index >= len(patern):
        return 1

    amount_of_fits = 0
    for key in keys:
        if patern[index:index+len(key)] == key:
            makeable = can_be_made(patern, index=index+len(key))
            if makeable:
                amount_of_fits += makeable


    return amount_of_fits
    
    
    






print('Part 1')
print(solve(keys, paterns))
print("Part 2")
print(solve2(keys, paterns))
