class Monkey:
    def __init__(self, starting_items: list[int], operation: list, test, play_count = 0):
        self.starting_items = starting_items
        self.operation = operation
        self.test = test # index: 0 - divisible by, 1 - true, 2 - false
        self.play_count = play_count
    
    def show_info(self):
        print(self.starting_items)
        print(self.operation)
        print(self.test)
        print(self.play_count)
        print("---------")
    
    def divisible(self, worry_level):
        if int(worry_level) % int(self.test[0]) == 0:
            return True
        return False
    
def parse_file(line, index):
    if index == 0:
        return line[1]
    if index == 1:
        starting_items = line[2:]
        return starting_items
    elif index == 2:
        operation = line[4:]
        return operation
    elif index == 3:
        test = line[3]
        return test
    elif index == 4:
        return line[-1]
    elif index == 5:
        return line[-1]


def wrap_info(monkey_info):
    result = []
    result.append(monkey_info[1])
    result.append(monkey_info[2])
    result.append(monkey_info[3:])
    return result

def collect_all_data():
    monkeys = []
    index = 0
    monkey_info = []
    with open("day 11/data.txt") as file:
        for line in file:
            if line != "\n":
                line = line.strip().replace(",","")
                info = line.split(" ")
                monkey_info.append(parse_file(info, index))
            else:
                monkeys.append(Monkey(*wrap_info(monkey_info)))
                index = -1
                monkey_info = []
            index += 1
            
    monkeys.append(Monkey(*wrap_info(monkey_info)))
    return monkeys


def playing(monkeys, temp = 0):
    worry_level = 0
    for _ in range(10000):
        for i in range(len(monkeys)):
            for item_worry in monkeys[i].starting_items:
                op = monkeys[i].operation[0]
                num = monkeys[i].operation[1]
                if num != "old":
                    num = int(num)
            
                worry_level = int(item_worry)
                if op == "+": 
                    if isinstance(num, int):
                        worry_level += int(num)
                    else:
                        worry_level += worry_level
                elif op == "*":
                    if isinstance(num, int):
                        worry_level *= int(num)
                    else:
                        worry_level *= worry_level

                worry_level = worry_level % temp
                
                if monkeys[i].divisible(worry_level):
                    where = int(monkeys[i].test[1])
                    monkeys[where].starting_items.append(worry_level)
                else:
                    where = int(monkeys[i].test[2])
                    monkeys[where].starting_items.append(worry_level)
                monkeys[i].play_count += 1
            monkeys[i].starting_items.clear()

monkeys = collect_all_data()

temp = 1
for x in monkeys:
    temp *= int(x.test[0])
playing(monkeys,temp)
for x in monkeys:
    x.show_info()

play_count = sorted([monkey.play_count for monkey in monkeys])
print(play_count[-1]*play_count[-2])
