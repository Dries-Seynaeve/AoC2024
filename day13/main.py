def parse_input(lines):
    prizes = []
    game = {}
    for line in lines:
        if not len(line) == 0:
            line_list = line.split()
            if line_list[0].__eq__("Button"):
                x = int(line_list[2][1:-1])
                y = int(line_list[3][1:])
                if line_list[1].__eq__("A:"):
                    game["A"] = [x, y]
                else:
                    game["B"] = [x, y]
            else:
                x = int(line_list[1][2:-1])
                y = int(line_list[2][2:])
                game["prize"] = [x, y]
        else:
            prizes.append(game)
            game = {}
    prizes.append(game)
    return prizes



def get_tokens(game):

    A = game["A"]
    B = game["B"]
    prize = game["prize"]
    tokens = 0
    if not A[1]*B[0] == B[1]*A[0]:
        beta = (prize[0]*A[1] - prize[1]*A[0]) // (B[0]*A[1]-B[1]*A[0])
        alpha = (prize[0] - beta*B[0]) // A[0]

        if all(alpha*x + beta*y == p for (p,x,y) in zip(prize, A,B)):
            tokens += alpha*3+beta

    return tokens





with open("input.txt") as f:
    lines = f.readlines()

lines = [line.strip() for line in lines]

if __name__ == "__main__":

    print("Part 1")
    games = parse_input(lines)
    print(sum(get_tokens(game) for game in games))
    print("Part 2")
    for game in games:
        game["prize"] = [x + 10000000000000 for x in game["prize"]]
    print(sum(get_tokens(game) for game in games))
    


