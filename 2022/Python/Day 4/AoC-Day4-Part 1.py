def D4P1(input):
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
    formatted.append([[temp[0],temp[1]],[temp[2],temp[3]]])
  
  output = 0
  for group in formatted:
    if (group[0][0] <= group[1][0] and group[0][1] >= group[1][1]) or (group[0][0] >= group[1][0] and group[0][1] <= group[1][1]):
      output += 1


  return output


assert(D4P1('D4 Test.txt')==2),"Function does not match example given"

print(D4P1('D4 Input.txt'))