#P4 AoC 2021

def AOC4(Input):
    input_file = open(Input,"r")
    InputListChar1= input_file.read().splitlines()

    aim = 0
    horizontal = 0
    depth = 0

    for i in InputListChar1:
        if i.split()[0] == 'forward':
            horizontal += int(i.split()[1])
            depth += aim * int(i.split()[1])
        elif i.split()[0] == 'down':
            aim += int(i.split()[1])
        elif i.split()[0] == 'up':
            aim += -int(i.split()[1])
        else:
            return "Unknown Command Found"
    
    return horizontal* depth

assert AOC4("D2 Test.txt") == 900, "Function does not match example given"

if __name__ == "__main__":
    print(AOC4("D2 Input.txt"))