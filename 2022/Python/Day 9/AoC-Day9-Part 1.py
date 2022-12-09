def D9P1(input):
  file = open(input,'r')
  file_list = file.read().splitlines()

  # x,y
  head = [0,0]
  tail = [0,0]
  tail_pos_dict = {'0,0':1}
  for move in file_list:
    move_list = move.split(' ')
    for positions in range(int(move_list[1])):
      if move_list[0] == 'U':
        head[1] += 1
      elif move_list[0] == 'D':
        head[1] -= 1
      elif move_list[0] == 'R':
        head[0] += 1
      elif move_list[0] == 'L':
        head[0] -= 1   

      if (abs(head[0]-tail[0]) + abs(head[1]-tail[1])) == 3:
        if abs(head[0]-tail[0]) == 1:
          tail[0] = head[0]
        else:
          tail[1] = head[1]
      if (abs(head[0]-tail[0])>1 or abs(head[1]-tail[1])>1):
        if head[0]-tail[0] > 1:
          tail[0] += 1
        elif head[0]-tail[0] < -1:
          tail[0] -= 1
        elif head[1]-tail[1] > 1:
          tail[1] += 1
        elif head[1]-tail[1] < -1:
          tail[1] -= 1
      if str(tail[0])+','+str(tail[1]) not in tail_pos_dict:
        tail_pos_dict[str(tail[0])+','+str(tail[1])] = 1
      else:
        tail_pos_dict[str(tail[0])+','+str(tail[1])] += 1

  return len(tail_pos_dict)

assert(D9P1('D9 Test.txt') == 13), "Function does not match example given"

print(D9P1('D9 Input.txt'))

