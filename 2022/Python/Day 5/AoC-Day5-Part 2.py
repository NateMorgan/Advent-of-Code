def D5P2(input):
  input_file = open(input,'r')
  input_list = input_file.read().splitlines()

  for line in range(len(input_list)):
    if input_list[line] == '':
      crate_section = input_list[:line]
      instruction_section = input_list[line+1:]
      break
  
  num_stacks = max(list(map(lambda x: int(x),crate_section[-1].split('  '))))
  crate_height = len(crate_section) - 1
  crate_list = []
  for i in range(num_stacks):
    stack_list = []
    for j in range(crate_height-1,-1,-1):
      if crate_section[j][1+4*i] != ' ':
        stack_list.append(crate_section[j][1+4*i])
    crate_list.append(stack_list)
  
  instruct_list = []
  for instruct in instruction_section:
    instruction = instruct[5:].split(' ')
    for crates in range(int(instruction[0]),0,-1):
      crate_list[int(instruction[4])-1].append(crate_list[int(instruction[2])-1].pop(-crates))
    instruct_list.append([int(instruction[0]),int(instruction[2]),int(instruction[4])])

  output = ''
  for stack in crate_list:
    output += stack.pop()

  return output

assert(D5P2('D5 Test.txt') == 'MCD'), "Function does not match example provided"

if __name__ == '__main__':
  print(D5P2('D5 Input.txt'))


