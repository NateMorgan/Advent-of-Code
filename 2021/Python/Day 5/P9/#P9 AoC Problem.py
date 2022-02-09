#P9 AoC Problem

def format(Input):
    input_file = open(Input)
    raw_data = input_file.read().splitlines()

    formatted_data1 = []
    for i in raw_data:
        formatted_data1.append(i.split(" -> "))

    formatted_data2 = []
    for i in formatted_data1:
        for j in range(len(i)):
            if j == 0:
                temp = i[j].split(",")
            else:
                formatted_data2.append([list(map(int,temp)),list(map(int,i[j].split(",")))])

    vert_hor_lines = []
    for i in formatted_data2:
        if i[0][0] == i[1][0] or i[0][1] == i[1][1]:
            vert_hor_lines.append(i)

    return vert_hor_lines

def line_to_points(input):
    output = []
    # if x is equal
    if input[0][0] == input[1][0]:
        if input[0][1] < input[1][1]:
            for j in range(input[0][1], input[1][1]+1):
                output.append([input[0][0],j])
        if input[0][1] > input[1][1]:
            for j in range(input[0][1], input[1][1]-1,-1):
                output.append([input[0][0],j])
    # if y is equal
    if input[0][1] == input[1][1]:
        if input[0][0] < input[1][0]:
            for j in range(input[0][0], input[1][0]+1):
                output.append([j,input[0][1]])
        if input[0][0] > input[1][0]:
            for j in range(input[0][0], input[1][0]-1,-1):
                output.append([j,input[0][1]])
    return output

def overlap(input):
    grid = []
    for row in range(1000):
        grid.append([])
        for col in range(1000):
            grid[row].append(0)
    for i in input:
        current = line_to_points(i)
        for point in current:
            grid[point[0]][point[1]] += 1
    sum = 0
    for row in grid:
        for col in row:
            if col > 1:
                sum += 1

    return sum

def main(Input):
    return overlap(format(Input))

assert main("D5 Test.txt") == 5, "Function does not match example given"

if __name__ =="__main__":
    print(main("D5 Input.txt"))