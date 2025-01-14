with open("input.txt") as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]

class Map2():
    def __init__(self, lines, columns):
        self.map = [["."]*2*columns for i in range(2*lines)]

    def add_Wall(self, x, y):
        wall = Wall(x, y)
        self.map[x][2*y]   = wall
        self.map[x][2*y+1] = wall

    def add_crate(self, x, y):
        cratel = Crate_L(x, y)
        crater = Crate_R(x, y)
        self.map[x][2*y] = cratel
        self.map[x][2*y+1] = crater

    def add_robot(self, x, y):
        self.x = x
        self.y = 2*y

    def move(self, dx, dy):
        if dx == 0:
            value = self.map[self.x][self.y]
            if isinstance(value, Wall):
                return False
            elif isinstance(value, Crate):
                delta = dy
                while isinstance(self.map[self.x][self.y+delta], Crate):
                    delta += dy
                return not isinstance(self.map[self.x, self.y+delta], Wall)
            else:
                return False

        if dy == 0:
                
        print(dx, dy)

    def move_left(self):
        self.move(0, -1)

    def print(self):
        for (i, row) in enumerate(self.map):
            line = ""
            for j, c in enumerate(row):
                if i == self.x and j == self.y:
                    line += "@"
                elif isinstance(c, Wall):
                    line += "#"
                elif isinstance(c, Crate_L):
                    line += "["
                elif isinstance(c, Crate_R):
                    line += "]"
                else:
                    line += "."
            print(line)
        




class Map():
    
    def __init__(self, lines, columns):
        self.lines = lines
        self.columns = columns

        self.map = [["."]*columns for i in range(lines)]
        self.walls = []
        self.crates = []

    def get_score(self):
        score = 0
        for i, line in enumerate(self.map):
            for j, c in enumerate(line):
                if isinstance(c, Crate):
                    score += i*100 + j
        return score
            

    def add_Wall(self, x, y):
        wall = Wall(x, y)
        self.walls.append(wall)
        self.map[x][y] = wall


    def add_crate(self, x, y):
        crate = Crate(x, y)
        self.crates.append(crate)
        self.map[x][y] = crate


    def add_robot(self, x, y):
        self.x = x
        self.y = y

    def movable(self, dx, dy):
        new_x = self.x + dx
        new_y = self.y + dy

        if isinstance(self.map[new_x][new_y], Wall):
            return False
        elif isinstance(self.map[new_x][new_y], Crate):
            while isinstance(self.map[new_x][new_y], Crate):
                new_x += dx
                new_y += dy
            if isinstance(self.map[new_x][new_y], Wall):
                return False
            else:
                return True
        else:
            return True

    def move_up(self):
        self.move(-1, 0)

    def move_down(self):
        self.move(1, 0)

    def move_left(self):
        self.move(0, -1)

    def move_right(self):
        self.move(0, 1)

    def move(self, dx, dy):
        if isinstance(self.map[self.x+dx][self.y+dy], Wall):
            return
        elif isinstance(self.map[self.x+dx][self.y+dy], Crate):
            if self.movable(dx, dy):
                self.x += dx
                self.y += dy

                delta_y = dy
                delta_x = dx
                while isinstance(self.map[self.x+delta_x][self.y+delta_y], Crate):
                    delta_y += dy
                    delta_x += dx
                self.map[self.x+delta_x][self.y+delta_y] = Crate(self.x+delta_x, self.y+delta_y)
                self.map[self.x][self.y] = "."
            else:
                return
        else:
            self.x += dx
            self.y += dy

    def print(self):
        for (i, row) in enumerate(self.map):
            line = ""
            for j, c in enumerate(row):
                if i == self.x and j == self.y:
                    line += "@"
                elif isinstance(c, Wall):
                    line += "#"
                elif isinstance(c, Crate):
                    line += "O"
                else:
                    line += "."
            print(line)









    
class Tile():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Wall(Tile):
    def __init__(self, x, y):
        super().__init__(x, y)

    def __repr__(self):
        return "#"

class Crate(Tile):
    def __init__(self, x, y):
        super().__init__(x, y)

    def __repr__(self):
        return "O"

class Crate_L(Crate):
    def __init__(self, x, y):
        super().__init__(x, y)

    def __repr__(self):
        return "["

class Crate_R(Crate):
    def __init__(self, x, y):
        super().__init__(x, y)

    def __repr__(self):
        return "]"



def parse_input(lines, map):

    directions = ""
    fill_map = True

    for i, line in enumerate(lines):
        if fill_map:
            for j, char in enumerate(line):
                if char.__eq__("#"):
                    map.add_Wall(i, j)
                elif char.__eq__("O"):
                    map.add_crate(i, j)
                elif char.__eq__("@"):
                    map.add_robot(i, j)
        else:
            directions += line
        if line == "":
            fill_map = False

    return map, directions

def move_robot(map, directions):
    for c in directions:
        #map.print()
        if c.__eq__("<"):
            map.move_left()
        elif c.__eq__(">"):
            map.move_right()
        elif c.__eq__("^"):
            map.move_up()
        elif c.__eq__("v"):
            map.move_down()
        else:
            print('ERROR')





if __name__ == "__main__":
    map = Map(len(lines), len(lines[0]))
    map, directions = parse_input(lines, map)
    # move_robot(map, directions)
    # print("Part 1")
    # print(map.get_score())
    print("Part 2")
    map = Map2(len(lines), len(lines[0]))
    map, directions = parse_input(lines, map)
    move_robot(map, directions)

    
