with open("day 6/data.txt") as file:
    start = 0
    index = 14
    buffer = file.read()
    for i in range(len(buffer)-13):
        if len(set(buffer[start:index])) == 14:
            print(index)
            break
        start += 1
        index += 1