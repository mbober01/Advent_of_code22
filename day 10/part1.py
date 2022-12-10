with open("day 10/data.txt") as file:
    x = 1
    cycles_to_register = [20+(x * 40) for x in range(6)]
    print(cycles_to_register)
    signal_strengths = []
    num_of_cycles = 0
    for cycle in file:
        cycle = cycle.strip().split(" ")
        if cycle[0].startswith("a"):
            v = int(cycle[1])
            for _ in range(2):
                num_of_cycles += 1
                if num_of_cycles in cycles_to_register:
                    signal_strengths.append(x*num_of_cycles)
            x += v
        else:
            num_of_cycles += 1
            if num_of_cycles in cycles_to_register:
                    signal_strengths.append(x*num_of_cycles)
            

print(signal_strengths)
print(sum(signal_strengths))
            
            
            
            
            
        #     v = int(cycle[1])
        #     addx.append([v,2])
        #     addx[0][1] -= 1

        # if addx[0][1] == 0:
        #     x += addx.pop(0)[0]
    
            
        # if num_of_cycles in cycles_to_register:
        #     print(x*num_of_cycles)
            
        
        # print(x)
        # print(num_of_cycles)
        # print("-------")
            
               
                  
            
            
            
            
            
            
            
            
            
            
 #     addx.append([v, 2])
            
        # if addx:
        #     if addx[index_add][1] == 0:
        #         x += addx[index_add][0]
        #         index_add += 1        
        #     addx[index_add][1] -= 1
            
        # num_of_cycles += 1