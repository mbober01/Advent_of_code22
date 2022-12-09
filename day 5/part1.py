def create_crates():
    with open("day 5/data.txt") as file:
        stacks = file.readlines()
        crates = []
        for stack in stacks:
            if stack == "\n":
                break
            crates.append(stack)


    size = int(crates[-1].strip().split(" ")[-1])
    cargo = [[] for x in range(size)]
    space_count = 0
    for i in range(size):
        added = 0
        space_count = 0
        for crate in crates[i]:
            if crate.isalpha():
                index = (space_count+added)//4
                added += 1
                cargo[index].append(crate)
            else:
                space_count += 1
                
    return cargo


cargo_crane = create_crates()

with open("day 5/data.txt") as file:
    while file.readline() != "\n":
        continue

    procedure = file.readlines()
    for instruction in procedure:
        crane_proc = instruction.split(" ")
        how_many = int(crane_proc[1])
        away = int(crane_proc[3])-1
        to = int(crane_proc[5])-1
        for crate in range(how_many):
            cargo_crane[to].insert(0, cargo_crane[away].pop(0))


result = ""
for crate in cargo_crane:
    result += crate[0]

print(result)


