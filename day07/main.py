def part1(lines):
    totals = []
    numbers = []
    total_true_1 = 0
    total_true_2 = 0
    for line in lines:
        line = line.split(":")
        total = int(line[0])
        numbers = [int(x) for x in line[1].split()]

        if can_be_true(total, numbers):
            total_true_1 += total
        if can_be_true(total, numbers, False):
            total_true_2 += total
    return total_true_1, total_true_2
    



def can_be_true(value, numbers, part1=True):

    if len(numbers) == 1:
        return value == numbers[0]
    else:

        sub_list_sum = numbers[1:].copy()        
        sub_list_sum[0] += numbers[0]
        use_sum = can_be_true(value, sub_list_sum, part1)

        sub_list_prod = numbers[1:].copy()
        sub_list_prod[0] *= numbers[0]
        use_prod = can_be_true(value, sub_list_prod, part1)

        sub_list_con = numbers[1:].copy()
        sub_list_con[0] = int(str(numbers[0]) + str(sub_list_con[0]))
        use_con = can_be_true(value, sub_list_con, part1)

        if part1:
            return use_sum or use_prod
        else:
            return use_sum or use_prod or use_con




    







if __name__ == "__main__":

    with open("input.txt") as f:
        lines = f.readlines()
    lines = [line.strip() for line in lines]
    result = part1(lines)

    print("Part 1:")
    print(result[0])
    print("Part 2:")
    print(result[1])

    
