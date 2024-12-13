import numpy as np

with open('input.txt') as f:
    lines = f.readlines()

lines = np.array([ np.array([int(x) for x in line.split()]) for line in lines])
linea, lineb = np.transpose(lines)


def part1(line1, line2):
    line1 = np.sort(line1)
    line2 = np.sort(line2)

    difference = [abs(x) for x in (line1 - line2)]
    return np.sum(difference)

def part2(line1, line2):
    unique, counts = np.unique(line2, return_counts=True)
    line2 = dict(zip(unique, counts))

    line1 = line1[np.array([x in line2 for x in line1])]
    return np.sum([x*line2[x] for x in line1])



if __name__ == "__main__":
    print("Part 1")
    print(part1(linea, lineb))
    print(" ")
    print("part 2")
    print(part2(linea, lineb))
    
    




