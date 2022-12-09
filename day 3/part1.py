def common_item(half1, half2):
    for x in half1:
        if x in half2:
            return x


with open("day 3/data.txt", 'r') as file:
    sum = 0
    rucksacks = file.readlines()
    for rucksack in rucksacks:
        rs_size = len(rucksack)
        half1 = rucksack[:int(rs_size/2)]
        half2 = rucksack[int(rs_size/2):]
        common = common_item(half1, half2)
        if ord(common) >= ord("a"):
            prio = ord(common) - ord("a") + 1
        else:
            prio = ord(common) - ord("A") + 27
        sum += prio
print(sum)