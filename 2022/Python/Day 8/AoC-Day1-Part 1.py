def D8P1(input):
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
    check = -1
    for col_idx in range(col_num):
      if matrix[row_idx][col_idx] > check:
        new_row.append(1)
        check = matrix[row_idx][col_idx]
      else:
        new_row.append(0)
    right_vis.append(new_row)

  left_vis = []
  for row_idx in range(row_num):
    new_row = []
    check = -1
    for col_idx in range(col_num-1,-1,-1):
      if matrix[row_idx][col_idx] > check:
        new_row.insert(0,1)
        check = matrix[row_idx][col_idx]
      else:
        new_row.insert(0,0)
    left_vis.append(new_row)

  down_vis = []
  for col_idx in range(col_num):
    new_col = []
    check = -1
    for row_idx in range(row_num):
      if matrix[row_idx][col_idx] > check:
        new_col.append(1)
        check = matrix[row_idx][col_idx]
      else:
        new_col.append(0)
    down_vis.append(new_col)

  up_vis = []
  for col_idx in range(col_num):
    new_col = []
    check = -1
    for row_idx in range(row_num-1,-1,-1):
      if matrix[row_idx][col_idx] > check:
        new_col.insert(0,1)
        check = matrix[row_idx][col_idx]
      else:
        new_col.insert(0,0)
    up_vis.append(new_col)

  combined_vis = []
  for row_idx in range(row_num):
    new_row = []
    for col_idx in range(col_num):
      if left_vis[row_idx][col_idx] or right_vis[row_idx][col_idx] or down_vis[col_idx][row_idx] or up_vis[col_idx][row_idx]:
        new_row.append(1)
      else:
        new_row.append(0)
    combined_vis.append(new_row)

  output = 0
  for row in combined_vis:
    for col in row:
      output += col

  return output


assert(D8P1('D8 Test.txt')==21), "Function does not match example given"

print(D8P1('D8 Input.txt'))