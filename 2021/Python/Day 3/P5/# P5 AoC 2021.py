#P5 AoC 2021

def AOC3(Input):

    input_file = open(Input,"r")
    InputListChar1= input_file.read().splitlines()

    one_count =[]

    for i in range(len(InputListChar1)):
        for char in range(len(InputListChar1[i])):
            if i == 0:
                one_count.append(int(InputListChar1[i][char]))
            else:
                one_count[char]+=int(InputListChar1[i][char])

    most = []
    for i in one_count:
        most.append(i/len(InputListChar1))

    gamma = ''
    epsilon = ''

    for i in most:
        if i > .5:
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon +='1'

    power = int(gamma,2) * int(epsilon,2)

    return power

assert AOC3("D3 Test.txt") == 198, "Function does not match example given"

if __name__ == "__main__":
    print(AOC3("D3 Input.txt"))