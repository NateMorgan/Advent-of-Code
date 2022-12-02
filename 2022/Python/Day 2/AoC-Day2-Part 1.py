def D2P1(Input):
    input_file = open(Input,"r")
    InputList = input_file.read().splitlines()

    score = {
      'A':1,
      'B':2,
      'C':3,
      'X':1,
      'Y':2,
      'Z':3
    }
      # Rock A 1 vs Paper Y 2     P2 Win Diff:-1
      # Rock A 1 vs Scissor Z 3   P1 Win Diff:-2

      #Scissor C 3 vs Rock X 1 .  P2 Win Diff:2
      #Scissor C 3 vs Paper Y 2   P1 Win Diff:1

      #Paper B 2 vs Rock X 1      P1 Win Diff:1
      #Paper B 2 vs Scissor Z 3   P2 Win Diff:-1

    total_score = 0
    for line in InputList:
      opponent_score = score[line[0]]
      my_score = score[line[2]]
      if opponent_score == my_score:
        total_score += 3
      elif (opponent_score - my_score) in [-1,2]:
        total_score += 6
      total_score += my_score

    return total_score

assert D2P1("D2 Test.txt") == 15, "Function does not pass example given"

if __name__ == "__main__":
    print(D2P1("D2 Input.txt"))