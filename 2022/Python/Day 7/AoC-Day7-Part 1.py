import time

def D7P1(input):
  file = open(input,'r')
  file_list = file.read().splitlines()

  folder_dict = {}
  active_folders = []
  unique_folders = []
  record = True
  for command in file_list:
    if command[0] == '$':
      if command[2:4] == 'cd' and command[5:] != '..':
        folder_path = "-".join(active_folders) + command[5:]
        active_folders.append(folder_path)
        if folder_path not in unique_folders:
          record = True
          unique_folders.append(folder_path)
          folder_dict[folder_path] = 0
        else:
          record = False
      elif command[5:] == '..':
        active_folders.pop()
    elif command[0:3] != 'dir' and record: 
      temp = command.split(' ')
      for folder in active_folders:
        folder_dict[folder] += int(temp[0])

  output = 0
  for folder in folder_dict:
    if folder_dict[folder] <= 100000:
      output += folder_dict[folder]
  return output

assert(D7P1('D7 Test.txt') == 95437), "Function does not match example given"
assert(D7P1('D7 Test 2.txt') == 99999), "Function does not match example found"

print(D7P1('D7 Input.txt'))