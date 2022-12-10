def print_crt(result):
    for x in result:
        for i in range(40):
            print(x[i],end="")
        print()


with open("day 10/data.txt") as file:
    x = 1
    num_of_cycles = 0
    result = [[] for _ in range(6)]
    new_row = [x*40+1 for x in range(1,6)]
    column = 0
    position = 0
    print(new_row)
    print(result)
    for cycle in file:
        cycle = cycle.strip().split(" ")
        if cycle[0].startswith("a"):
            v = int(cycle[1])
            for _ in range(2):
                num_of_cycles += 1
                position += 1
                if num_of_cycles in new_row:
                    column += 1
                    position = 0
                if abs(position - x) > 1:
                    result[column].append(".")
                else:
                    result[column].append("#")
            x += v
        else:
            num_of_cycles += 1
            position += 1
            if num_of_cycles in new_row:
                    column += 1
                    position = 0
            if abs(position - x) > 1:
                result[column].append(".")
            else:
                result[column].append("#")


print_crt(result)