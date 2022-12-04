def D4P2(input):
  input_file = open(input,'r')
  input_list = input_file.read().splitlines()

  formatted = []
  for line in input_list:
    temp = []
    pair = line.split(',')
    for range in pair:
      string_list = range.split('-')
      for string in string_list:
        temp.append(int(string))
    formatted.append([temp[0],temp[1],temp[2],temp[3]])
  
  output = 0
  for group in formatted:
    if (group[1] >= group[2]) and (group[3] >= group[0]):
      output += 1

  return output


assert(D4P2('D4 Test.txt')==4),"Function does not match example given"

print(D4P2('D4 Input.txt'))