with open("input.txt") as f:
    lines = [line.strip() for line in f.readlines()]

class Tile():
    def __init__(self, x, y, passable):
        self.x = x
        self.y = y
        self.parent = None
        self.child = None
        self.passable = passable
        self.cost = 0

    def __repr__(self):
        return "[{}, {}]".format(self.x, self.y)

class Grid():
    def __init__(self):
        self.grid = self.make_grid()
        self.solve_maze()
        self.cheats = self.get_cheat_positions()



    def get_cheat_positions(self):
        cheats = []
        cell =self.start

        while not cell == self.end:
            neighbours = [tile for tile in self.get_neighbours(cell) if not tile.passable]
            
            cheats.append([(tile, self.get_next(cell, tile).cost - cell.cost-2)   for tile in neighbours if self.get_next(cell, tile) is not None and self.get_next(cell,tile).passable])


            cell = cell.child
        cheats = [x for cheat in cheats for x in cheat if x[1] >= 0]
        return list(set(cheats))

    def get_next(self, cell, tile):
        x = 2*tile.x - cell.x
        y = 2*tile.y - cell.y

        if x in range(len(lines[0])) and y in range(len(lines)):
            return self.get_tile(x, y)
        else:
            return None


    def make_grid(self):
        grid = []
        for j, line in enumerate(lines):
            for i, c in enumerate(line):
                tile = Tile(i, j, c != "#")
                grid.append(tile)
                if c == "S":
                    self.start = tile
                if c == "E":
                    self.end = tile
        return grid

    def solve_maze(self):
        cell = self.start
        cost = 0
        while not cell == self.end:
            parent = cell
            neighbours = [tile for tile in self.get_neighbours(cell) if tile.passable]
            neighbours = [cell for cell in neighbours if not cell == parent.parent ]

            cell = neighbours[0]
            cell.parent = parent
            parent.child = cell
            cost += 1
            cell.cost = cost

            
            

    def get_neighbours(self, tile):
        x0 = tile.x
        y0 = tile.y
        neighbours = []
        if x0 >= 1:
            neighbours.append(self.get_tile(x0-1, y0))
        if y0 >= 1:
            neighbours.append(self.get_tile(x0, y0-1))
        if x0 < len(lines[0])-1:
            neighbours.append(self.get_tile(x0+1, y0))
        if y0 < len(lines)-1:
            neighbours.append(self.get_tile(x0, y0+1))
        return neighbours
            

    def get_tile(self, x, y):
        return self.grid[y*len(lines[0])+x]






        
        
if __name__ == "__main__":
    grid = Grid()
    cheats = {}
    for ch in grid.cheats:
        c = ch[1]
        if c in cheats:
            cheats[c] += 1
        else:
            cheats[c] = 1

    keys = [cheats[k] for k in cheats.keys() if k >= 100]
    print("Part 1")
    print(sum(keys))
