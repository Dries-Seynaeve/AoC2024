import heapq

with open("input.txt") as f:
    lines = [line.strip() for line in f.readlines()]

class Cell():
    def __init__(self, x, y, reachable):
        self.reachable = reachable
        self.x = x
        self.y = y
        self.parent = None
        self.g = 0
        self.h = 0
        self.f = 0

    def __lt__(self, other):
        self.f < other.f
        
class Solution():
    def __init__(self, path, score, final):
        self.path = path
        self.score = score

class Grid():

    def __init__(self):
        self.paths = {}
        self.cells = []
        self.grid_height = len(lines)
        self.grid_width = len(lines[0])
 
    def init_grid(self, walls, start, end):
        for x in range(self.grid_height):
            for y in range(self.grid_width):
                reachable = not (x,y) in walls
                self.cells.append(Cell(x, y, reachable))
        x, y = start
        self.start     = self.get_cell(x, y)

        x, y = end
        self.end = self.get_cell(x, y)

    def get_cell(self, x, y):
        return self.cells[x * self.grid_height + y]

    def get_adject_cells(self, cell):
        cells = []
        if cell.x < self.grid_width-1:
            cells.append(self.get_cell(cell.x+1, cell.y))
        if cell.y > 0:
            cells.append(self.get_cell(cell.x, cell.y-1))
        if cell.x > 0:
            cells.append(self.get_cell(cell.x-1, cell.y))
        if cell.y < self.grid_height-1:
            cells.append(self.get_cell(cell.x, cell.y+1))
        return cells


    def solve(self, cell=None):
        if cell is None:
            cell = self.start

        print(self.get_adject_cells(cell))
        print(cell.x, cell.y)


    



class AStar():
    
    def __init__(self):
        self.opened = []
        heapq.heapify(self.opened)
        self.closed = set()
        self.cells = []
        self.grid_height = len(lines)
        self.grid_width = len(lines[0])
 
    def init_grid(self, walls, start, end):
        for x in range(self.grid_height):
            for y in range(self.grid_width):
                reachable = not (x,y) in walls
                self.cells.append(Cell(x, y, reachable))
        x, y = start
        self.start     = self.get_cell(x, y)
        self.start.parent = [Cell(x-1, y, False)]

        x, y = end
        self.end = self.get_cell(x, y)

    def get_heuristic(self, cell):
        return abs(cell.x - self.end.x) + 1000 + abs(cell.y - self.end.y)

    def get_cell(self, x, y):
        return self.cells[x * self.grid_height + y]

    def get_value_of_step(self, cell, adj):

        parent = cell.parent[-1]
        
        if (parent.x - cell.x) == (cell.x - adj.x) and \
           (parent.y - cell.y) == (cell.y - adj.y):
            return 1
        else:
            return 1001
        
            
            

    def get_adject_cells(self, cell):
        cells = []
        if cell.x < self.grid_width-1:
            cells.append(self.get_cell(cell.x+1, cell.y))
        if cell.y > 0:
            cells.append(self.get_cell(cell.x, cell.y-1))
        if cell.x > 0:
            cells.append(self.get_cell(cell.x-1, cell.y))
        if cell.y < self.grid_height-1:
            cells.append(self.get_cell(cell.x, cell.y+1))
        return cells



    def display_path(self):
        cell = self.end
        amount_of_tile = 1
        while cell.parent is not None:
            amount_of_tile += 1
            cell = cell.parent

            if len(cell) == 1:
                cell = cell[0]
                print("path: cell: {}, {}".format(cell.x, cell.y))

        print("amound of tile: ", amount_of_tile)

    
    def update_cell(self, adj, cell, replace):

        adj.g = cell.g + self.get_value_of_step(cell, adj)
        adj.h = self.get_heuristic(adj)
        if replace or adj.parent is None:
            adj.parent = [cell]
        else:
            adj.parent.append(cell)
        adj.f = adj.h + adj.g

                

            

    def process(self):
        # add starting cell to open heap queue
        heapq.heappush(self.opened, (self.start.f, self.start))
        while len(self.opened):
            # pop cell from heap queue
            f, cell = heapq.heappop(self.opened)

            # add cell to closed list so we don't process it twice
            self.closed.add(cell)
            # if ending cell, display found path
            if cell is self.end:
                print("Score: ", cell.g)

                self.display_path()
                break
            # get adjacent cells for cell
            adj_cells = self.get_adject_cells(cell)

            for adj_cell in adj_cells:
                if adj_cell.reachable and adj_cell not in self.closed:
                    if (adj_cell.f, adj_cell) in self.opened:
                        # if adj cell in open list, check if current path is
                        # better then the one previously found for this adj
                        # cell

                        if adj_cell.g >= (cell.g + self.get_value_of_step(cell, adj_cell)):
                            if adj_cell.g > (cell.g + self.get_value_of_step(cell, adj_cell)):
                                self.update_cell(adj_cell, cell, True)
                            else:
                                self.update_cell(adj_cell, cell, False)
                    else:
                        self.update_cell(adj_cell, cell, False)

                        # add adj cell to open list
                        heapq.heappush(self.opened, (adj_cell.f, adj_cell))

        
        



        
        

if __name__ == "__main__":
    walls = [(x, y) for (y, line) in enumerate(lines) for (x, c) in enumerate(line) if c.__eq__("#")]

    start = [(x, y) for (y, line) in enumerate(lines) for (x, c) in enumerate(line) if c.__eq__("S")]
    end = [(x, y) for (y, line) in enumerate(lines) for (x, c) in enumerate(line) if c.__eq__("E")]

    # astar = AStar()
    # astar.init_grid(walls, start[0], end[0])

    # astar.process()

    solve = Grid()
    solve.init_grid(walls, start[0], end[0])
    solve.solve()


