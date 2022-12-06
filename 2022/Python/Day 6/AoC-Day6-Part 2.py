def D6P2(input):
  file = open(input,'r')
  file_input = file.read().splitlines()[0]

  for index in range(len(file_input)-13):
    test_list = []
    for char in file_input[index:index+14]:
      if char not in test_list:
        test_list.append(char)
      else:
        break
    if len(test_list) == 14:
      return index + 14
  return -1

assert(D6P2('D6 Test.txt') == 26), "Function does not match example given"

if __name__ == '__main__':
  print(D6P2('D6 Input.txt'))