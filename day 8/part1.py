def get_forest():
    with open("day 8/data.txt", "r") as file:
        lines = file.readlines()
        forest = [[] for x in range(len(lines))]
        i = 0
        for row in lines:
            row = row.strip()
            for tree in row:
                forest[i].append(tree)
            i += 1
    
    return forest

forest = get_forest()

visible_count = len(forest[0])*2 + len(forest)*2 - 4
is_visible = True
direction_count = 0 # needs to be 4 at the end for tree to not be visible
current_tree = 0
# rows
for x in range(1,len(forest)-1):
    # columns
    for y in range(1, len(forest[0])-1):
        direction_count = 0
        is_visible = True
        current_tree = forest[x][y]
        # checking up-down
        for i in range(x):
            if current_tree <= forest[i][y]:
                direction_count += 1
                break
        
        for i in range(x+1,len(forest)):
            if current_tree <= forest[i][y]:
                direction_count += 1
                break
            
        # checking left-right
        for j in range(y):
            if current_tree <= forest[x][j]:
                direction_count += 1
                break
        
        for j in range(y+1, len(forest[0])):
             if current_tree <= forest[x][j]:
                direction_count += 1
                break
        
        if direction_count == 4:
            is_visible = False
        
        if is_visible:
            visible_count += 1
        
print(visible_count)