#P20 AoC Problem

def main(Input):
    raw_data = open(Input)
    formatted_data = raw_data.read().splitlines()

    open_close = {
        "(":")",
        "[":"]",
        "{":"}",
        "<":">",
    }

    open_bracket = ["(","[","{","<"]

    formmatted_data2 = []
    for i in formatted_data:
        closing_list = []
        write = True
        for j in i:
            if j in open_bracket:
                closing_list.append(open_close[j])
            else:
                if j != closing_list.pop():
                    write = False
        if write:
            formmatted_data2.append(i)

    points = {
        ")": 1,
        "]": 2,
        "}": 3,
        ">": 4
    }

    line_score = []
    for i in formmatted_data2:
        closing_list = []
        score = 0
        for j in i:
            if j in open_bracket:
                closing_list.append(open_close[j])
            else:
                closing_list.pop()
        closing_list.reverse()
        for p in closing_list:
            score *= 5
            score += points[p]
        line_score.append(score)

    line_score.sort()

    return line_score[int(len(formmatted_data2)/2)]

assert main("D10 Test.txt") == 288957, "Function does not match example given"

if __name__ == "__main__":
    print(main("D10 Input.txt"))