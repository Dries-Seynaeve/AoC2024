def part1(lines):
    return sum(valueOfLine(line)[0] for line in lines)

def part2(lines):
    enable = True
    value = 0
    for line in lines:
        val, e = valueOfLine(line, enable)
        value += val
        enable = e
    return value


            


def valueOfLine(line, doEnabled=True):
    """
    We parse the line and extract the elements between "mul(" and ")"
    and return their product if possible.

    For part 2 we added a flag doEnabled that swich the extraction on/off 
    """
    result = 0
    idx_b = 0
    while idx_b < len(line):
        # Multiply values of we detect a mul(*)
        if line[idx_b:idx_b+4].__eq__("mul(") and doEnabled:
            idx_t = idx_b+4
            while line[idx_t] != ")":
                idx_t += 1
            input = line[idx_b+4:idx_t].split(",")
            if all(x.isdigit() for x in input):
                result += int(input[0])*int(input[1])
                idx_b = idx_t-1
        # Toggle the doEnabled flag
        elif line[idx_b:idx_b+7].__eq__("don't()"):
            doEnabled = False
            idx_b = idx_b+6
        elif line[idx_b:idx_b+4].__eq__("do()"):
            doEnabled = True
            idx_b = idx_b+3
        idx_b += 1
        
    return result, doEnabled

if __name__ == "__main__":
    with open('input.txt') as f:
        lines = f.readlines()
    print("Part 1:")
    print(part1(lines))
    print("Part 2:")
    print(part2(lines))
