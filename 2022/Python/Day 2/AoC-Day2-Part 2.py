def D2P2(Input):
    input_file = open(Input,"r")
    InputList = input_file.read().splitlines()

    score = {
      'A':1,
      'B':2,
      'C':3,
      'X':0,
      'Y':3,
      'Z':6
    }
      # Rock A 1 vs Scissor Z 3   P1 Win Diff:-2
      #Paper B 2 vs Rock X 1      P1 Win Diff:1
      #Scissor C 3 vs Paper Y 2   P1 Win Diff:1

      # Rock A 1 vs Paper Y 2     P2 Win Diff:-1
      #Paper B 2 vs Scissor Z 3   P2 Win Diff:-1
      #Scissor C 3 vs Rock X 1 .  P2 Win Diff:2

    total_score = 0
    for line in InputList:
      opponent_score = score[line[0]]
      result = score[line[2]]
      total_score += result
      if result == 3:
        total_score += opponent_score
      elif result == 6:
        total_score += (opponent_score + 1) if opponent_score != 3 else 1
      else:
        total_score += (opponent_score - 1) if opponent_score != 1 else 3

    return total_score

assert D2P2("D2 Test.txt") == 12, "Function does not pass example given"

if __name__ == "__main__":
    print(D2P2("D2 Input.txt"))