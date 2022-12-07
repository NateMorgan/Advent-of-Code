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

  total = 70000000
  unused = (total - folder_dict['/'])
  need = 30000000 - unused
  smallest = total
  for folder in folder_dict:
    if folder_dict[folder] >= need and folder_dict[folder] < smallest:
      smallest = folder_dict[folder]
  return smallest

assert(D7P1('D7 Test.txt') == 24933642), "Function does not match example given"

print(D7P1('D7 Input.txt'))