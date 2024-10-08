def D1P2(Input):
    input_file = open(Input, "r")
    InputList = input_file.read().splitlines()

    elf_list = []

    current = 0
    for line in InputList:
        if line != '':
            current += int(line)
        else:
            elf_list.append(current)
            current = 0
    elf_list.append(current)
    elf_list.sort(reverse=True)
    return sum(elf_list[0:3])


assert D1P2("D1 Test.txt") == 45000, "Function does not pass example given"


if __name__ == "__main__":
    print(D1P2("D1 Input.txt"))
