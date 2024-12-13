import numpy as np

with open("input.txt") as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]



def get_number_of_sides(area):

    amount_of_lines = 0
    
    # Horizontal lines
    for i in range(len(lines)):
        elements_in_line = [pos[1] for pos in area if pos[0] == i ]
        if len(elements_in_line) == 0:
            continue
        i_min = min(elements_in_line)
        i_max = max(elements_in_line)

        while i_min <= i_max:
            amount_of_lines += 1
            while i_min in elements_in_line:
                i_min += 1
            while i_min not in elements_in_line and i_min <= i_max:
                i_min += 1

    print(amount_of_lines)
    # vertical lines
    for i in range(len(lines[0])):
        elements_in_line = [pos[0] for pos in area if pos[1] == i ]

        if len(elements_in_line) == 0:
            continue

        i_min = min(elements_in_line)
        i_max = max(elements_in_line)

        while i_min <= i_max:
            amount_of_lines += 1
            while i_min in elements_in_line:
                i_min += 1
            while i_min not in elements_in_line and i_min <= i_max:
                i_min += 1
    return amount_of_lines








def get_sides(area):
    neighbours = []
    for square in area:
        n_neighbours = 0
        if (square[0]-1,square[1]) in area:
            n_neighbours += 1
        if (square[0],square[1]-1) in area:
            n_neighbours += 1
        if (square[0]+1,square[1]) in area:
            n_neighbours += 1
        if (square[0],square[1]+1) in area:
            n_neighbours += 1
        neighbours.append(n_neighbours)
    
    return sum(4 - x for x in neighbours)
        
            
        


def main(lines):
    searched_areas = np.full((len(lines), len(lines[0])), False)
    area = {}
    price_1 = 0
    price_2 = 0
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if not searched_areas[i,j]:
                area = get_area(i,j)
                sides = get_sides(area)
                number_sides = get_number_of_sides(area)
                a = len(area)

                for pos in area:
                    searched_areas[pos[0], pos[1]] = True
                print(lines[i][j], number_sides)
                price_1 += a*sides
                price_2 += a*number_sides
    return price_1, price_2
            

def get_group_neighbours(i, j):
    neighbours = []
    if i > 0 and lines[i-1][j].__eq__(lines[i][j]):
        neighbours.append((i-1,j))
    if j > 0 and lines[i][j-1].__eq__(lines[i][j]):
        neighbours.append((i,j-1))
    if i < len(lines)-1 and lines[i+1][j].__eq__(lines[i][j]):
        neighbours.append((i+1,j))
    if j < len(lines[i])-1 and lines[i][j+1].__eq__(lines[i][j]):
        neighbours.append((i,j+1))
    return neighbours



def get_new_neighbours(pos, old_neighbours):

    i, j = pos
    neighbours = get_group_neighbours(i,j)
    new_neighbours = [ x for x in neighbours if all(x[0]!=y[0] or x[1]!=y[1] for y in old_neighbours)]
    return new_neighbours


def get_area(i, j):
    old_neighbours = [(i,j)]
    new_neighbours = get_new_neighbours((i,j), old_neighbours)

    for x in new_neighbours:
        old_neighbours.append(x)

    while not len(new_neighbours) == 0:
        new_new_neighbours = []
        for n in new_neighbours:
            for x in get_new_neighbours(n, old_neighbours):
                old_neighbours.append(x)
                new_new_neighbours.append(x)
                
        new_neighbours = new_new_neighbours    

            
    for x in new_neighbours:
        old_neighbours.append(x)
    
    return old_neighbours
            
            
            
    

    

    
    

if __name__ == "__main__":
    print(main(lines))
