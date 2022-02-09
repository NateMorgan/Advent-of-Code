#P11 AoC Problem

def model(day,input):
    raw_data = open(input)
    formatted_data = list(map(int,raw_data.read().split(",")))
    days = day
    new_list = formatted_data
    for days in range(days):
        new_fish = 0
        for i in range(len(new_list)):
            if new_list[i] == 0:
                new_fish += 1
                new_list[i] = 7
            new_list[i] += -1
        for i in range(new_fish):
            new_list.append(8)
    return len(new_list)

assert model(18,"D6 Test.txt") == 26, "Function does not match example given"
assert model(80,"D6 Test.txt") == 5934, "Function does not match example given"

if __name__ == "__main__":
    print(model(80,"D6 Input.txt"))

        