# part 1
lista = []
with open("day 1/data.txt", 'r') as file:
    lines = file.readlines()
    sum_of_callories = 0
    for line in lines:
        if line != "\n":
            sum_of_callories+=int(line)
        
        elif line == "\n":
            lista.append(sum_of_callories)
            sum_of_callories = 0
    
    lista.append(sum_of_callories)
            
highest_callories = max(lista)
print("Part 1 result")
print(highest_callories)


# part 2
sum_of_top_callories = 0
for x in range(3):
    highest_callories = max(lista)
    lista.remove(highest_callories)
    sum_of_top_callories += highest_callories

print("Part 2 result")
print(sum_of_top_callories)

