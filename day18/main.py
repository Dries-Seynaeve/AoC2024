with open("input.txt") as f:
    lines = [line.strip() for line in f.readlines()]

def get_walls(amount_of_bytes):
    return [(int(lines[i].split(",")[0]), int(lines[i].split(",")[1])) for i in range(amount_of_bytes)]

amount_lines = 6
amount_columns = 6


neighbours = [(-1,0),(1,0),(0,-1),(0,1)]



class Cell():
    def __init__(self, x, y, passable=True):
        self.x = x
        self.y = y
        self.passable = passable
        self.f = 0
        self.g = amount_lines - 
        self.h = 0
        self.parent = None

    def __repr__(self):
        return "({x}, {y}): {h}".format(x=self.x, y=self.y, h=self.h)

class Astar():
    def __init__(self):
        self.maze = []

    def create_maze(self, walls):
        for i in range(amount_lines):
            for j in range(amount_columns):
                if (j, i) in walls:
                    cell = Cell(j, i, False)
                else:
                    cell = Cell(j, i, True)
                self.maze.append(cell)
        self.start = self.maze[0]
        self.start.g = amount_lines + amount_columns
        self.start.h = self.start.f + self.start.g

        self.end = self.maze[-1]

    def get_cell(self, i, j):
        return self.maze[i*amount_columns + j]

    def get_neighbours(self, cell):
        neighbours = []
        if cell.x > 1:
            neighbours.append(self.get_cell(cell.x-1, cell.y))
        if cell.y > 1:
            neighbours.append(self.get_cell(cell.x, cell.y-1))
        if cell.x < amount_columns:
            neighbours.append(self.get_cell(cell.x+1, cell.y))
        if cell.y < amount_lines:
            neighbours.append(self.get_cell(cell.x, cell.y+1))
        neighbours = [x for x in neighbours if x.passable]
        return neighbours

    def solve(self):
        open = [self.start]
        closed = set()

        while open:
            cell = open.pop()
            closed.add(cell)

            if cell == self.end:
                return

            neighbours = self.get_neighbours(cell)
            for neigh_cell in neighbours:
                if neigh_cell in closed:
                    continue
                else:
                    if neigh_cell in open:
                        if neigh_cell.h < cell.h + 1:
                            neigh_cell.h = cell.h+1
                            neigh_cell.parent = cell
                    else:
                        neigh_cell.h
                        
                print(neigh_cell)




    




def solve(walls):
    start = ((0, 0), (0, amount_lines+amount_columns)) # x, y, cost
    end = ((amount_lines,amount_columns),(None, None))

    open = []
    open.append(start)
    closed = set()
    sort_list = lambda x : sum(x[1])
    while open:
        tile, cost = open.pop()
        closed.add((tile, cost))
        print(tile)
        if tile == end[0]:
            print("HAHAHAAH")
            break


        # Get neigbours
        neigh_cell = [(tile[0]+i[0], tile[1]+i[1]) for i in neighbours]
        # We stay in the grid
        neigh_cell = [x for x in neigh_cell if x[0] in range(amount_columns) and x[1] in range(amount_lines)]
        # We make sure we don't cross into walls
        neigh_cell = [x for x in neigh_cell if not x in walls ]

        print(" ")
        print(tile)
        for neigh in neigh_cell:
            neigh_cost = (cost[0]+1, amount_columns - neigh[0] + amount_lines - neigh[1])
            neigh_cell = (neigh, neigh_cost)

            if len(open) == 0:
                open.append(neigh_cell)
            else:
                pos, values = zip(*open)
                print("\t", neigh in pos)
                print("\t",pos)
                print(neigh)
                

        open.sort(key=sort_list, reverse=True)


        # sort the open list




        



        # Open for every neighbours and check cost
        
        
        

wall = get_walls(12)
astar = Astar()
astar.create_maze(wall)
astar.solve()
