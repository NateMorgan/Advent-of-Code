#P1 AoC 2021

def AOC1(Input):
    input_file = open(Input,"r")
    InputListChar = input_file.read().splitlines()
    InputList = []

    for j in InputListChar:
        InputList.append(int(j))

    increase = 0
    for i in range(len(InputList)-1):
        if InputList[i+1] > InputList[i]:
            increase += 1
    return increase

assert AOC1("D1 Test.txt") == 7, "Function does not pass example given"

if __name__ == "__main__":
    print(AOC1("D1 Input.txt"))