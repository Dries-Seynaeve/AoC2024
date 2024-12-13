import numpy as np

def part1(lines, part1=True):
    antennas  = {}
    antinodes = {}
    n_lines = range(len(lines))
    n_char  = range(len(lines[0]))
    for (i, line) in enumerate(lines):
        for (j, c) in enumerate(line):
            if not c.__eq__("."):
                if c in antennas.keys():
                    antennas[c].append(np.array([i,j]))
                else:
                    antennas[c] = [np.array([i,j])]

    # get antinodes
    for frequency in antennas.keys():
        antinodes[frequency] = []
        antennas_of_freq = antennas[frequency]
        for i in range(len(antennas_of_freq)):
            antenna1 = antennas_of_freq[i]
            for j in range(i+1, len(antennas_of_freq)):
                antenna2 = antennas_of_freq[j]
                diff = antenna1 - antenna2

                if part1:
                    pnt1 = antenna1 + diff
                    pnt2 = antenna2 - diff


                    if (pnt1[0] in n_lines) and (pnt1[1] in n_char):
                        antinodes[frequency].append(pnt1)
                    if (pnt2[0] in n_lines) and (pnt2[1] in n_char):
                        antinodes[frequency].append(pnt2)
                else:
                    pnt1 = antenna1.copy()
                    pnt2 = antenna2.copy()

                    while (pnt1[0] in n_lines) and (pnt1[1] in n_char):
                        antinodes[frequency].append(pnt1.copy())
                        pnt1 += diff
                    while (pnt2[0] in n_lines) and (pnt2[1] in n_char):
                        antinodes[frequency].append(pnt2.copy())
                        pnt2 -= diff

    all_antinodes = np.concatenate(list(antinodes.values()))
    stripped_antinodes = []
    for x in all_antinodes:
        if not any([(x == y).all() for y in stripped_antinodes]):
            stripped_antinodes.append(x)
    return len(stripped_antinodes)
            










if __name__=="__main__":
    with open("input.txt") as f:
        lines = f.readlines()
    lines = [list(line.strip()) for line in lines]
    print("Part 1")
    print(part1(lines, True))
    print("Part 2")
    print(part1(lines, False))
