#P3 AoC 2021

def AOC3(Input):

    input_file = open(Input,"r")
    InputListChar1= input_file.read().splitlines()

    horizontal = 0
    depth = 0
    for i in InputListChar1:
        if i.split()[0] == 'forward':
            horizontal += int(i.split()[1])
        elif i.split()[0] == 'down':
            depth += int(i.split()[1])
        elif i.split()[0] == 'up':
            depth += -int(i.split()[1])
        else:
            return "Unknown Command Found"
    
    return horizontal * depth

assert AOC3("D2 Test.txt") == 150, "Function does not match example given"

if __name__ == "__main__":
    print(AOC3("D2 Input.txt"))