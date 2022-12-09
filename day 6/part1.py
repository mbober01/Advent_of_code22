with open("day 6/data.txt") as file:
    start = 0
    index = 4
    buffer = file.read()
    for i in range(len(buffer)-3):
        if len(set(buffer[start:index])) == 4:
            print(index)
            break
        start += 1
        index += 1