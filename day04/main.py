
def part1(lines):
    total_xmas = 0
    total_x_mas = 0
    for idx_l in range(len(lines)):
        for idx_c in range(len(lines[idx_l])):
            if lines[idx_l][idx_c].__eq__("X"):
                total_xmas += amount_of_XMAS(lines, idx_l, idx_c)
            if lines[idx_l][idx_c].__eq__("A"):
                total_x_mas += is_X_MAS(lines, idx_l, idx_c)
    return total_xmas, total_x_mas


def is_X_MAS(lines, idx_l, idx_c):
    if idx_l > 0 and idx_l < len(lines)-1:
        if idx_c > 0 and idx_c < len(lines[idx_l])-1:
            diag1 = "".join([lines[idx_l-1+l][idx_c-1+l] for l in range(3)])
            diag2 = "".join([lines[idx_l-1+l][idx_c+1-l] for l in range(3)])
            diag1 = diag1.__eq__("MAS") or diag1.__eq__("SAM")
            diag2 = diag2.__eq__("MAS") or diag2.__eq__("SAM")

            return int(diag1 and diag2)
    return 0     

def amount_of_XMAS(lines, idx_l, idx_c):
    amount = 0
    # Horizontal (forward and backwards)
    if idx_c <= len(lines[idx_l])-4:
        amount += lines[idx_l][idx_c:idx_c+4].__eq__("XMAS")
    if idx_c >=3:
        amount += lines[idx_l][idx_c-3:idx_c+1].__eq__("SAMX")

    # Vertical (forward and backwards)
    if idx_l <= len(lines)-4:
        amount += "".join([l[idx_c] for l in lines[idx_l:idx_l+4]]).__eq__("XMAS")
    if idx_l >=3:
        amount += "".join([l[idx_c] for l in lines[idx_l-3:idx_l+1]]).__eq__("SAMX")


    # Diagonal (forward and backwards)
    if idx_l >= 3 and idx_c >= 3:
        amount += "".join([lines[idx_l-l][idx_c-l] for l in range(4)]).__eq__("XMAS")
    if idx_l >= 3 and idx_c <= len(lines[idx_l])-4:
        amount += "".join([lines[idx_l-l][idx_c+l] for l in range(4)]).__eq__("XMAS")
    if idx_l <= len(lines)-4 and idx_c >= 3:
        amount += "".join([lines[idx_l+l][idx_c-l] for l in range(4)]).__eq__("XMAS")
    if idx_l <= len(lines)-4 and idx_c <= len(lines[idx_l])-4:
        amount += "".join([lines[idx_l+l][idx_c+l] for l in range(4)]).__eq__("XMAS")
    return amount 













if __name__=="__main__":
    with open('input.txt') as f:
        lines = f.readlines()
    lines = [line.strip() for line in lines]
    result = part1(lines)
    print("Part 1")
    print(result[0])
    print("Part 2")
    print(result[1])    
    
