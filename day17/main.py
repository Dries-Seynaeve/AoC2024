with open("input.txt") as f:
    lines = [line.strip() for line in f.readlines()]

A = int(lines[0].split()[-1])
B = int(lines[1].split()[-1])
C = int(lines[2].split()[-1])

pointr = 0



def combo(x):
    match x:
        case 4:
            return A
        case 5:
            return B
        case 6:
            return C
        case _:
            return x
            
def move_pnt():
    global pointr
    pointr += 2

def adv(x):
    global A
    move_pnt()
    A = int(A / (2**combo(x)))
    return

def bxl(x):
    global B
    move_pnt()
    B = B ^ x


def bst(x):
    global B
    move_pnt()
    new_value = combo(x) % 8
    B = new_value
    return

def jnz(x):
    global pointr
    global A

    if A == 0:
        move_pnt()
        return
    else:
        pointr = x
        return

def bxc(x):
    global B, C
    move_pnt()
    B = B ^ C
    return

def out(x):
    move_pnt()
    return combo(x) % 8

def bdv(x):
    global A
    move_pnt()
    B = int(A / (2**combo(x)))
    return

def cdv(x):
    global A, C
    move_pnt()
    C = int(A / (2**combo(x)))
    return

instructions = [adv, bxl, bst, jnz, bxc, out, bdv, cdv]

def run_program(program, A):

    global pointr
    global B,C

    results = []
    while pointr < len(program):

        fnc_idx = program[pointr]
        argument = program[pointr+1]

        function = instructions[fnc_idx]
        value = function(argument)
        if value is not None:
            results.append(str(value))
    pointr = 0

    B = int(lines[1].split()[-1])
    C = int(lines[2].split()[-1])
    return ",".join(results)


program = [int(x) for x in lines[4].split()[-1].split(",")]
print("Part 1:")
print(run_program(program, A))


print("Part 2:")

