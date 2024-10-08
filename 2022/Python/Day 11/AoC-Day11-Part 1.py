class Monkey:
  def __init__(self, items, operation, test_num,test_pass_true,test_pass_false):
    self.items = [int(x) for x in items.split(', ')]
    self.operation = eval(operation)
    self.test_num = int(test_num)
    self.test_pass_true = int(test_pass_true)
    self.test_pass_false = int(test_pass_false)

  def __str__(self):
    print_statement = ""
    for item in self.items:
      print_statement += "Monkey inspects an item with a worry level of " + str(item)+ "\n"
      print_statement += "Worry level is now " + self.operation(item) + '\n'
    return print_statement



def D11P1(input):
  file = open(input,'r')
  file_input = file.read().split('\n\n')
  monkey_list = []
  for monkey in file_input:
    monkey_dets = monkey.split('\n')
    items = monkey_dets[1].split(': ')[1]
    operation = monkey_dets[2].split(': ')[1]
    test_num = monkey_dets[3].split('by ')[1]
    test_pass_true = monkey_dets[4].split('monkey ')[1]
    test_pass_false = monkey_dets[5].split('monkey ')[1]
    monkey_list.append(Monkey(items,operation,test_num,test_pass_true,test_pass_false))
  return monkey_list[0]

# assert(D11P1('D11 Test.txt' == 10605)), "Function does not match example given"

print(D11P1('D11 Test.txt'))