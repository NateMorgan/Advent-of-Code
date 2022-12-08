def D8P2(input):
  file = open(input,'r')
  file_list = file.read().splitlines()

  col_num = len(file_list[0])
  row_num = len(file_list)

  matrix = []
  for row_idx in range(row_num):
    new_row = []
    for char in file_list[row_idx]:
      new_row.append(int(char))
    matrix.append(new_row)

  right_vis = []
  for row_idx in range(row_num):
    new_row = []
    for col_idx in range(col_num):
      check = matrix[row_idx][col_idx]
      viewing_distance = 0
      for tree in range(col_idx+1,col_num):
        viewing_distance += 1
        if matrix[row_idx][tree] >= check:
          break
      new_row.append(viewing_distance)
    right_vis.append(new_row)

  left_vis = []
  for row_idx in range(row_num):
    new_row = []
    for col_idx in range(col_num-1,-1,-1):
      check = matrix[row_idx][col_idx]
      viewing_distance = 0
      for tree in range(col_idx-1,-1,-1):
        viewing_distance += 1
        if matrix[row_idx][tree] >= check:
          break
      new_row.insert(0,viewing_distance)
    left_vis.append(new_row)

  down_vis = []
  for col_idx in range(col_num):
    new_col = []
    for row_idx in range(row_num):
      check = matrix[row_idx][col_idx]
      viewing_distance = 0 
      for tree in range(row_idx+1,row_num):
        viewing_distance += 1
        if matrix[tree][col_idx] >= check:
          break
      new_col.append(viewing_distance)
    down_vis.append(new_col)

  up_vis = []
  for col_idx in range(col_num):
    new_col = []
    for row_idx in range(row_num-1,-1,-1):
      check = matrix[row_idx][col_idx]
      viewing_distance = 0
      for tree in range(row_idx-1,-1,-1):
        viewing_distance += 1
        if matrix[tree][col_idx] >= check:
          break
      new_col.insert(0,viewing_distance)
    up_vis.append(new_col)

  combined_vis = []
  for row_idx in range(row_num):
    new_row = []
    for col_idx in range(col_num):
      new_row.append(right_vis[row_idx][col_idx] * left_vis[row_idx][col_idx] * up_vis[col_idx][row_idx] * down_vis[col_idx][row_idx])
    combined_vis.append(new_row)

  output = 0
  for row in combined_vis:
    for col in row:
      if col > output:
        output = col

  return output


assert(D8P2('D8 Test.txt')==8), "Function does not match example given"

print(D8P2('D8 Input.txt'))