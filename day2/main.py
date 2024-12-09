import numpy as np

with open('input.txt') as f:
    lines = f.readlines()

lines = [np.array([int(x) for x in line.split()]) for line in lines]

def part1(lines):
    return sum(1 if isSafe(line) else 0 for line in lines)


def part2(lines):
    return sum(1 if isSafeWithDampener(line) else 0 for line in lines)

        

def isSafeWithDampener(line):

    for i in np.arange(len(line)):
        if isSafe(np.delete(line,i)):
            return True
    return False

def isSafe(line):
    diff = line[:-1]-line[1:]
    decOrInc = np.all([x > 0 for x in diff]) or np.all([x < 0 for x in diff])
    maxDiff = max([abs(x) for x in diff]) <= 3
    return maxDiff and decOrInc
    



if __name__ == "__main__":
    print("Part 1")
    print(part1(lines))
    print(" ")
    print("Part 2")
    print(part2(lines))
