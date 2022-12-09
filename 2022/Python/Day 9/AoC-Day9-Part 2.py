def follow(before,after):
  output = after
  if (abs(before[0]-after[0]) + abs(before[1]-after[1])) == 3:
    if abs(before[0]-after[0]) == 1:
      output[0] = before[0]
    else:
      output[1] = before[1]
  if (abs(before[0]-after[0])>1 and abs(before[1]-after[1])>1):
    if before[0]-after[0] == 2 and before[1]-after[1] == 2:
      output[0] += 1
      output[1] += 1
    elif before[0]-after[0] == 2 and before[1]-after[1] == -2:
      output[0] += 1
      output[1] -= 1
    elif before[0]-after[0] == -2 and before[1]-after[1] == 2:
      output[0] -= 1
      output[1] += 1
    elif before[0]-after[0] == -2 and before[1]-after[1] == -2:
      output[0] -= 1
      output[1] -= 1
  elif (abs(before[0]-after[0])>1 or abs(before[1]-after[1])>1):
    if before[0]-after[0] > 1:
      output[0] += 1
    elif before[0]-after[0] < -1:
      output[0] -= 1
    elif before[1]-after[1] > 1:
      output[1] += 1
    elif before[1]-after[1] < -1:
      output[1] -= 1
  return output


def D9P2(input,num_knots):
  file = open(input,'r')
  file_list = file.read().splitlines()

  # x,y
  head = [0,0]
  tail = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
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
      for i in range(len(tail)):
        if i == 0:
          tail[0] = follow(head,tail[0])
        else:
          tail[i] = follow(tail[i-1],tail[i])
      if str(tail[num_knots-2][0])+','+str(tail[num_knots-2][1]) not in tail_pos_dict:
        tail_pos_dict[str(tail[num_knots-2][0])+','+str(tail[num_knots-2][1])] = 1
      else:
        tail_pos_dict[str(tail[num_knots-2][0])+','+str(tail[num_knots-2][1])] += 1
  return len(tail_pos_dict)

assert(D9P2('D9 Test 2.txt',10) == 36), "Function does not match example given"
assert(D9P2('D9 Test.txt',10) == 1), "Function does not match example given"

print(D9P2('D9 Input.txt',10))

