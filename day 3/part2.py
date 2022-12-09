def common_item(group):
    for x in group[0]:
        if x in group[1] and x in group[2]:
            return x


with open("day 3/data.txt", 'r') as file:
    sum = 0
    rucksacks = file.readlines()
    group_size = 0
    group = []
    for rucksack in rucksacks:
        group.append(rucksack)
        group_size += 1
        if group_size == 3:
            common = common_item(group)
            if ord(common) >= ord("a"):
                prio = ord(common) - ord("a") + 1
            else:
                prio = ord(common) - ord("A") + 27
            sum += prio
            group.clear()
            group_size = 0
print(sum)