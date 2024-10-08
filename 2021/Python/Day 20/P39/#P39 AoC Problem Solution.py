# P39 AoC Problem Solution

def main(Input, Enhances=1):
    raw = open(Input)
    formatted_data = raw.read().splitlines()

    enhance_algo = formatted_data[0]
    input_image = formatted_data[2:]

    binary_decode = {
        ".": 0,
        "#": 1
    }

    rev_binary_decode = {
        0: ".",
        1: "#"
    }

    binary_input = [[binary_decode[i] for i in row] for row in input_image]
    enhance_algo_binary = [binary_decode[i] for i in enhance_algo]

    for enhan in range(Enhances):

        if enhan == 0:
            n = 2
        else:
            n = 1

        if enhan == 0:
            pixel = 0
        else:
            pixel = binary_input[0][0]

        for p in range(n):
            binary_input.insert(0, [pixel]*(len(binary_input[pixel])))
            binary_input.append([pixel]*(len(binary_input[pixel])))
        for row in range(len(binary_input)):
            for k in range(n):
                binary_input[row].insert(0, pixel)
                binary_input[row].append(pixel)
        binary_output = [[i for i in row] for row in binary_input]
        for row in range(len(binary_input)):
            for col in range(len(binary_input[row])):
                enhance_num = ""
                if (col > 0) and (row > 0) and (row < len(binary_input)-1) and (col < len(binary_input[row])-1):
                    for i in range(-1, 2):
                        for j in range(-1, 2):
                            enhance_num += str(binary_input[row+i][col+j])
                else:
                    enhance_num = str(binary_input[row][col])*9
                binary_output[row][col] = enhance_algo_binary[int(
                    enhance_num, 2)]
        binary_input = [[i for i in row] for row in binary_output]
        image_output = [[rev_binary_decode[i]
                         for i in row] for row in binary_output]

    lit_count = sum(sum(x) for x in binary_output)

    return lit_count, image_output


assert main("D20 Test.txt", 2)[
    0] == 35, "Function does not match example given"

if __name__ == "__main__":
    print(main("D20 Input.txt", 2)[0])
