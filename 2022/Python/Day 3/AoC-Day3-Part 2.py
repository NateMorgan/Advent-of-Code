def D3P2 (input):
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
  for idx in range(int(len(input_list)/3)):
    bag1 = input_list[idx*3]
    bag2 = input_list[idx*3+1]
    bag3 = input_list[idx*3+2]
    for char in bag1:
      if char in bag2:
        if char in bag3:
          same_list.append(char)
          output += priority_dict[char]
          break
  

  return output

assert(D3P2('D3 Test.txt') == 70), "Function does not match example given"

if __name__ == '__main__':
  print(D3P2('D3 Input.txt'))