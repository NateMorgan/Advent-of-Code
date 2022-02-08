#P7 AoC Problem

def gamecreator(Input):
    
    input_file = open(Input)
    raw_data = input_file.read().splitlines()

    bingo_selection = raw_data.pop(0).split(",")

    board_list = []
    board_count = 0
    for i in raw_data:
        if i == '':
            board_list.append([])
            board_count += 1

        else:
            board_list[board_count-1].append(i.split())
    
    return board_list,bingo_selection

def bingo_winner(Boards,Selections):
    marked_board = Boards
    for num in Selections:
        for board in range(len(marked_board)):
            row_check = [True, True, True, True, True]
            column_check = [True, True, True, True, True]
            for row in range(len(marked_board[board])):
                for col in range(len(marked_board[board][row])):
                    if num == marked_board[board][row][col]:
                        marked_board[board][row][col] = 'X'
                    if marked_board[board][row][col] != 'X':
                        row_check[row] = False
                        column_check[col] = False
            if (True in row_check or True in column_check):
                sum = 0
                for i in range(len(marked_board[board])):
                    for j in range(len(marked_board[board][i])):
                        if marked_board[board][i][j] != 'X':
                            sum += int(marked_board[board][i][j])

                return(int(num)*sum)
            
def main(Input):
    return bingo_winner(gamecreator(Input)[0],gamecreator(Input)[1])

assert main("D4 Test.txt") == 4512, " Function does not match example given"

if __name__ == "__main__":
    print(main("D4 Input.txt"))
