def D10P2(input):
  file = open(input,'r')
  file_list = file.read().splitlines()

  X = 1
  cycle_list = [1]
  for instruct in range(len(file_list)):
    cycle_list.append(X)
    if file_list[instruct] != 'noop':
      cycle_list.append(X)
      X += int(file_list[instruct].split(' ')[1])
  cycle_list.append(X)

  crt = []
  for row in range(6):
    new_row = []
    for pixel in range(40):
      index = row*40 + pixel
      if abs(cycle_list[index+1] - pixel) < 2:
        new_row.append('#')
      else:
        new_row.append('.')
    crt.append("".join(new_row))
    print(crt[row])

print(D10P2('D10 Input.txt'))