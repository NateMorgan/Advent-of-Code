def D10P1(input):
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

  output = 0
  for cycle in range(20,240,40):
    output += cycle * cycle_list[cycle]
  return output

assert(D10P1('D10 Test.txt') == 13140)

print(D10P1('D10 Input.txt'))