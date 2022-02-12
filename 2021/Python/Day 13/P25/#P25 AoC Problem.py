#P25 AoC Problem

def createGrid(max_x, max_y):
    grid = []
    for y in range(max_y+1):
        grid.append([])
        for x in range(max_x+1):
            grid[y].append('.')
    return grid

# grid[y][x])

def fold_result(grid, fold):
    command = fold.split("=")
    if command[0] == 'x':
        end_grid = createGrid(int(command[1])-1,len(grid)-1)
        for y in range(len(end_grid)):
            for x in range(len(end_grid[y])):
                if grid[y][x] == '#' or grid[y][(2*int(command[1])-x)] == '#':
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

    coordinates =[]
    for i in range(len(formatted_data2)):
        coordinates.append(list(map(int,formatted_data2[i])))

    max_x = 1310
    max_y = 954

    start_grid = createGrid(max_x,max_y)

    for q in coordinates:
        start_grid[q[1]][q[0]] = '#'

    test = fold_result(start_grid,"x=655")

    count = 0
    for i in test:
        for y in i:
            if y =='#':
                count +=1

    return count

if __name__ == "__main__":
    print(main("D13 Input.txt"))
