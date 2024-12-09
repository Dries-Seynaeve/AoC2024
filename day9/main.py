def part1(line):

    express = get_disk_map(line)
    express = compatictify_string_part1(express)
    return file_checksum(express)

def part2(line):
    express = get_disk_map(line)
    express = compatictify_string_part2(express)
    return file_checksum(express)

def get_disk_map(line):
    files = line[::2]
    frees = line[1::2]
    i = 0
    express = []
    for (file, free) in zip(files,frees):
        express += [i]*int(file) + [None]*int(free)
        i += 1

    express += [i]*int(files[i])
    return express

def file_checksum(express):

    sum = 0
    for i in range(len(express)):
        if express[i] is not None:
            sum += i*int(express[i])
    return sum


def compatictify_string_part2(express):
    j2 = len(express)-1
    compact_string = express.copy()
    while j2 > 0:

        while express[j2] is None:
            j2 -= 1

        j1 = j2
        while express[j1] == express[j2]:
            j1 -= 1
        j1 += 1

        i1 = 0
        i2 = 0

        while ((i2 - i1) < (j2+1-j1)) and i1 < j1:
            i1 = i2

            while compact_string[i1] is not None:
                i1 += 1
            if i1 > j1:
                break;
            i2 = i1

            while compact_string[i2] is None:
                i2 += 1
        i2 -= 1



        if (i2 - i1) >= (j2 - j1):
            compact_string = compact_string[:i1] + compact_string[j1:j2+1] + compact_string[i1+j2-j1+1:]
            compact_string[j1:j2+1] = [None]*(j2+1-j1)
            
        j2 = j1-1

    return compact_string


        




def compatictify_string_part1(express):

    j = len(express)-1
    i = 0
    s = 0
    compact_exp = []
    
    while i < j:
        s = i
        while express[i] is not None:
            i += 1

        compact_exp += express[s:i]
        while express[j] is None:
            j -= 1
        compact_exp += [express[j]]

        i += 1
        j -= 1
    if express[i] is not None:
        compact_exp += [express[i]]
    return compact_exp

        



if __name__=="__main__":
    with open("input.txt") as f:
        lines = f.readlines()
    line = lines[0].strip()
    print("Part 1")
    print(part1(line))
    print("Part2")
    print(part2(line))
    
