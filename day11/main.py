from multiprocessing import Pool

        



def blink(value):
    n_digits = len(str(value))
    if value == 0:
        return [1]
    elif n_digits%2 == 0:
        half = n_digits//2
        return [int(str(value)[:half]), int(str(value)[half:])]
    else:
        return [2024*value]


def blink_line(line):
    values = line.keys()
    occurance = list(line.values())
    result = {}
    new_line = [blink(value) for value in values]
    for idx in range(len(values)):
        occurs = occurance[idx]
        for j in new_line[idx]:
            if j in result.keys():
                result[j] += occurs
            else:
                result[j] = occurs
    return result

def get_result(line, n):
    for i in range(n):
        line = blink_line(line)
    return sum(line.values())



if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()
    line = lines[0].strip()
    line = [int(x) for x in line.split()]
    line = {i:line.count(i) for i in line}



    print("Part 1")
    print(get_result(line, 25))
    print("Part 2")
    print(get_result(line, 75))
