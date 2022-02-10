#P14 AoC Problem

def main(Input):
    raw_data = open(Input)
    formatted_data = list(map(int,raw_data.read().split(",")))

    summary = [0] * 2000

    max = 0
    for i in formatted_data:
        if i > max:
            max = i
        summary[i] += 1

    summary_reduced = summary[:max+1]
    gas_cost = [0] * len(summary_reduced)
    for i in range(len(gas_cost)):
        for j in range(len(summary_reduced)):
            # (n*(n+1)) / 2 sum of 1 to n
            gas_cost[i] += int((abs((j-i))*(abs((j-i))+1)) * summary_reduced[j] / 2)

    return min(gas_cost)

assert main("D7 Test.txt") == 168, " Function does not match example given"

if __name__ == "__main__":
    print(main("D7 Input.txt"))