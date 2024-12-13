import numpy as np

def part1(lines):
    mask, is_path = get_path(lines)
    return len(lines)*len(lines[0]) - sum("".join(l).count(" ") for l in mask) - sum("".join(l).count("#") for l in mask)



def get_path(lines):
    # Find position
    (i0, j0) = find_position(lines)
    
    mask = np.full((len(lines), len(lines[0])), " ", dtype=object)
    mask[i0, j0] = "0"

    direction = ["up", "right", "down", "left"]
    j = 0
    while (i0 in range(len(lines)-1)) and (j0 in range(len(lines[0])-1)):
        (i1, j1) = move_guard((i0, j0), direction[j])

        if lines[i1][j1].__eq__("#"):
            mask[i1,j1] = "#"
            j += 1
            j = j % 4

        elif mask[i1, j1].__eq__(" "):
            mask[i1, j1] = str(j)
            (i0, j0) = (i1, j1)
        else:
            before = mask[i1, j1]
            after = str(j)
            if after in before:
                return mask, True
            else:
                mask[i1, j1] = before+after
            (i0, j0) = (i1, j1)
        reachEnd = (j0 == 0 and j == 3) or (j0 == len(lines[0])-1 and j==1) \
            or (i0 == 0 and j==2) or (i0 == len(lines) and j==0)
        if reachEnd:
            return mask, False

    return mask, False




def part2(lines):
    mask, is_loop = get_path(lines)

    mask = np.array([np.array([not (c.__eq__(" ") or c.__eq__("#"))for c in line]) for line in mask])

    i0, j0 = find_position(lines)
    mask[i0, j0] = False

    line, chars = np.indices((len(lines), len(lines[0])))
    hits = 0
    for l, c in zip(line[mask], chars[mask]):
        lines2 = lines.copy()
        lines2[l] = lines[l][:c]+"#"+lines[l][c+1:]
        path, is_loop = get_path(lines2)
        if is_loop:
            hits += 1

    return hits






def find_position(lines):
    for i in range(len(lines)):
        if "^" in lines[i]:
            for j in range(len(lines[i])):
                if lines[i][j].__eq__("^"):
                    return (i, j)
                    break
            break



def move_guard(position, direction ):
    match direction:
        case "up":
            return (position[0]-1, position[1])
        case "right":
            return (position[0], position[1]+1)
        case "down":
            return (position[0]+1, position[1])
        case "left":
            return (position[0], position[1]-1)



if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()
    lines = [line.strip() for line in lines]
    print("Part 1")
    print(part1(lines))
    print("Part 2")
    print(part2(lines))
