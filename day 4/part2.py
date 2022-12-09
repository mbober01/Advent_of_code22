pair_together = []
fully_contain = 0
with open("day 4/data.txt") as file:
    assignments = file.readlines()
    for assignment in assignments:
        pairs = assignment.strip().split(",")
        for pair in pairs:
            temp = pair.split("-")
            pair_together.append([x for x in range(int(temp[0]), int(temp[1])+1)])
        if any(x in pair_together[0] for x in pair_together[1]) or any(x in pair_together[1] for x in pair_together[0]):
            fully_contain += 1
        pair_together.clear()

print(fully_contain)