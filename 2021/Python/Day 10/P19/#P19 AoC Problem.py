#P19 AoC Problem

def main(Input):
    raw_data = open(Input)
    formatted_data = raw_data.read().splitlines()

    open_close = {
        "(":")",
        "[":"]",
        "{":"}",
        "<":">",
    }

    open_brackets = ["(","[","{","<"]

    formmatted_data2 = []
    for i in formatted_data:
        closing_list = []
        write = True
        for j in i:
            if j in open_brackets:
                closing_list.append(open_close[j])
            else:
                if j != closing_list.pop():
                    write = False
        if write:
            formmatted_data2.append(closing_list)

    points = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137
    }

    score = 0
    for i in formatted_data:
        closing_list = []
        for j in i:
            if j in open_brackets:
                closing_list.append(open_close[j])
            else:
                if j != closing_list.pop():
                    score += points[j]

    return score

assert main("D10 Test.txt") == 26397, "Function does not match example given"

if __name__ == "__main__":
    print(main("D10 Input.txt"))