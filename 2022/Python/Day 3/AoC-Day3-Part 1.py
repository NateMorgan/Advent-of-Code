def D3P1 (input):
  input_file = open(input,"r")
  input_list = input_file.read().splitlines()

  priority_dict = {}
  priority_num = 1
  for char in 'abcdefghijklmnopqrstuvwxyz':
    priority_dict[char] = priority_num
    priority_dict[char.upper()] = priority_num + 26
    priority_num += 1
  
  output = 0
  same_list = []
  for line in input_list:
    compartment1 = line[0:int(len(line)/2)]
    compartment2 = line[int(len(line)/2):]
    for char in compartment1:
      if char in compartment2:
        same_list.append(char)
        output += priority_dict[char]
        break
  

  return output

assert(D3P1('D3 Test.txt') == 157), "Function does not match example given"

if __name__ == '__main__':
  print(D3P1('D3 Input.txt'))