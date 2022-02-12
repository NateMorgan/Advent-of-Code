#P25 AoC Problem

def createGrid(max_x, max_y):
    grid = []
    for y in range(max_y+1):
        grid.append([])
        for x in range(max_x+1):
            grid[y].append('.')
    return grid

def foldResult(grid, fold):
    command = fold.split("=")
    if command[0] == 'x':
        end_grid = createGrid(int(command[1])-1,len(grid)-1)
        for y in range(len(end_grid)):
            for x in range(len(end_grid[y])):
                if grid[y][x] == '#' or grid[y][(2*int(command[1])-x)] == '#':
                    end_grid[y][x] = '#'
    elif command[0] == 'y':
        end_grid = createGrid(len(grid[0])-1,int(command[1])-1)
        for y in range(len(end_grid)):
            for x in range(len(end_grid[y])):
                if grid[y][x] == '#' or grid[(2*int(command[1])-y)][x] == '#':
                    end_grid[y][x] = '#'

    return end_grid

def main(Input):
    raw_data = open(Input)
    formatted_data = raw_data.read().splitlines()

    formatted_data2 =[]
    for i in range(len(formatted_data)):
        formatted_data2.append(formatted_data[i].split(","))

    folding = []
    for i in range(13):
        folding.append(formatted_data2.pop())

    folding.pop()
    folding.reverse()

    instructions = []

    for i in folding:
        tmp = i[0].split()
        instructions.append(tmp[2])

    coordinates = []
    for i in range(len(formatted_data2)):
        coordinates.append(list(map(int,formatted_data2[i])))

    max_x = 1310
    max_y = 954

    start_grid = createGrid(max_x,max_y)

    for q in coordinates:
        start_grid[q[1]][q[0]] = '#'

    # grid[y][x])

    for i in instructions:
        tmp_grid = foldResult(start_grid,i)
        start_grid = tmp_grid

    output = []
    for i in start_grid:
        output.append(' '.join(i))
    
    return output

if __name__ == "__main__":
    for i in main("D13 Input.txt"):
        print(i)
