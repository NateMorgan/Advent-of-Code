def D6P1(input):
  file = open(input,'r')
  file_input = file.read().splitlines()[0]

  for index in range(len(file_input)-3):
    test_list = []
    for char in file_input[index:index+4]:
      if char not in test_list:
        test_list.append(char)
      else:
        break
    if len(test_list) == 4:
      return index + 4
  return -1

assert(D6P1('D6 Test.txt') == 11), "Function does not match example given"

if __name__ == '__main__':
  print(D6P1('D6 Input.txt'))