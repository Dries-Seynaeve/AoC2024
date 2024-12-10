import numpy as np

def part1and2(lines):
    coords = []
    score = 0
    # get the trail stars
    coord_start = get_trail_start(lines)

    for coord in coord_start:
        result = get_trailheads_and_score(coord, 1, lines)
        coords += result[0]
        score  += result[1]
    return len(coords), score


def get_trailheads_and_score(coord, value, lines):
    l_max = len(lines)-1
    c_max = len(lines[0])-1
    score = 0
    l, c = coord
    positions = []


    filter = lambda x,y : any(pos[0]==x and pos[1]==y for pos in positions)

    if value == 9:
        if l > 0 and int(lines[l-1][c]) == 9:
            pos = np.array([l-1, c])
            positions.append(pos)
            score += 1
        if c > 0 and int(lines[l][c-1]) == 9:
            positions.append(np.array([l,c-1]))
            score += 1
        if l < l_max and int(lines[l+1][c]) == 9:
            positions.append(np.array([l+1,c]))
            score += 1
        if c < c_max and int(lines[l][c+1]) == 9:
            positions.append(np.array([l,c+1]))
            score += 1
        return strip(positions), score

    else:
        if l > 0 and int(lines[l-1][c]) == value:
            result = get_trailheads_and_score((l-1,c), value+1, lines)
            positions += result[0]
            score += result[1]
        if c < c_max and int(lines[l][c+1]) == value:
            result= get_trailheads_and_score((l, c+1), value+1, lines)
            positions += result[0]
            score += result[1]
        if l < l_max and int(lines[l+1][c]) == value:
            result = get_trailheads_and_score((l+1, c), value+1, lines)
            positions += result[0]
            score += result[1]
        if c > 0 and int(lines[l][c-1]) == value:
            result = get_trailheads_and_score((l,c-1), value+1, lines)
            positions += result[0]
            score += result[1]
        return strip(positions), score


def strip(score):
    stripped = []
    for i in score:
        if not any((i == j).all() for j in stripped):
            stripped.append(i)
    return stripped




def get_trail_start(lines):
    coord = []
    for l in range(len(lines)):
        for c in range(len(lines[l])):
            if int(lines[l][c]) == 0:
                coord.append((l, c))
    return coord

    





if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()
    lines = [line.strip() for line in lines]
    result = part1and2(lines)
    print("Part 1")
    print(result[0])
    print("Part 2")
    print(result[1])

