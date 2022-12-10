directions = {
    "R": [0,1],
    "L": [0,-1],
    "U": [1,0],
    "D": [-1,0]
}


# tells if tail has to go diagonal

def go_diagonal(head_pos, tail_pos):    
    if head_pos[0] != tail_pos[0] and head_pos[1] != tail_pos[1]:
        return True
    return False

with open("day 9/data.txt") as file:
    lines = file.readlines()
    head_pos = [0, 0] # x:y position of head atm
    tail_pos = [0, 0] # x:y position of tail atm
    visited = [[0, 0]]
    last_pos = head_pos[:]
    
    for line in lines:
        motion = line.strip().split(" ") # line of code giving instructions
        way = motion[0] # right, left, up, down
        length = int(motion[1]) # how long move
        for moves in range(length): # go step by step based on how big is length of move
            last_pos = head_pos[:]
            head_pos[0] += directions[way][0]
            head_pos[1] += directions[way][1]
            # if abs(abs(head_pos[0]) - abs(tail_pos[0])) > 1 or abs(abs(head_pos[1]) - abs(tail_pos[1])) > 1:
            if abs(head_pos[0] - tail_pos[0]) > 1 or abs(head_pos[1] - tail_pos[1]) > 1:
                # if go_diagonal(head_pos, tail_pos):
                tail_pos = last_pos[:]
                # else:
                #     tail_pos[0] += directions[way][0]
                #     tail_pos[1] += directions[way][1]
            
                
            if tail_pos not in visited:
                visited.append(tail_pos[:])
            

print(len(visited))
