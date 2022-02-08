#P6 AoC 2021

def Oxygen(Input):

    input_file = open(Input,"r")
    InputListChar1= input_file.read().splitlines()

    current_list = InputListChar1
    match = []
    for char in range(len(InputListChar1)):
        one_count = 0
        for i in current_list:
            one_count += int(i[char])
        if one_count/len(current_list) >= .5:
            match.append('1')
        else:
            match.append('0')
        for i in range(len(current_list)-1,-1,-1):
            if current_list[i][char] != match[char]:
                current_list.pop(i)
        
        if len(current_list) == 1:
            break

    return int(current_list[0],2)

def CO2(Input):

    input_file = open(Input,"r")
    InputListChar1= input_file.read().splitlines()

    current_list = InputListChar1
    match = []
    for char in range(len(InputListChar1)):
        one_count = 0
        for i in current_list:
            one_count += int(i[char])
        if one_count/len(current_list) >= .5:
            match.append('0')
        else:
            match.append('1')
        for i in range(len(current_list)-1,-1,-1):
            if current_list[i][char] != match[char]:
                current_list.pop(i)
        
        if len(current_list) == 1:
            break

    return int(current_list[0],2)

def main(Input):
    return Oxygen(Input)*CO2(Input)

assert Oxygen("D3 Test.txt") == 23, "Function does not match example given"
assert CO2("D3 Test.txt") == 10, "Function does not match example given"

if __name__ == "__main__":
    print(main("D3 Input.txt"))