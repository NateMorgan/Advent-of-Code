#P2 AoC 2021

def AOC2(Input):
    input_file = open(Input,"r")
    InputListChar1 = input_file.read().splitlines()
    InputList1 = []

    for j in InputListChar1:
        InputList1.append(int(j))
        
    InputList2 = []
    for k in range(len(InputList1)-2):
        InputList2.append((InputList1[k]+InputList1[k+1]+InputList1[k+2]))

    increase = 0
    for i in range(len(InputList2)-1):
        if InputList2[i+1] > InputList2[i]:
            increase += 1
    return increase

assert AOC2("D1 Test.txt") == 5, "Function does not pass example given"

if __name__ == "__main__":
    print(AOC2("D1 Input.txt"))