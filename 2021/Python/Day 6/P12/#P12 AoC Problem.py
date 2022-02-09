#P11 AoC Problem

def model2(day,input):
    raw_data = open(input)
    formatted_data = list(map(int,raw_data.read().split(",")))

    summary = [0,0,0,0,0,0,0,0,0]
    for i in formatted_data:
        summary[i] += 1
    prev_day = summary

    for days in range(day):
        new_day = [0,0,0,0,0,0,0,0,0]
        for i in range(len(prev_day)):
            if i == 0:
                new_day[8] += prev_day[i]
                new_day[6] += prev_day[i]
            else:
                new_day[i-1] += prev_day[i]
        prev_day = new_day
    sum = 0
    for i in prev_day:
        sum += i
    return sum

assert model2(256,"D6 Test.txt") == 26984457539, "Function does not match example given"

if __name__ == "__main__":
    print(model2(256,"D6 Input.txt"))