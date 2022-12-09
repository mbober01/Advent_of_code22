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

current_tree = 0
max_scenic_score = 0
# rows
for x in range(1,len(forest)-1):
    # columns
    for y in range(1, len(forest[0])-1):
        view_distance = [0,0,0,0] # scenic scores
        scenic_score = 1
        # index: 0 - up, 1 - down, 3 - left, 4 - right
        current_tree = forest[x][y]
        
        
        # checking up-down
        for i in range(x-1,-1,-1):
            if current_tree <= forest[i][y]:
                view_distance[0] += 1
                break
            else:
                view_distance[0] += 1
        
        for i in range(x+1,len(forest)):
            if current_tree <= forest[i][y]:
                view_distance[1] += 1
                break
            else:
                view_distance[1] += 1
            
        # checking left-right
        for j in range(y-1,-1,-1):
            if current_tree <= forest[x][j]:
                view_distance[2] += 1
                break
            else:
                view_distance[2] += 1
        
        for j in range(y+1, len(forest[0])):
            if current_tree <= forest[x][j]:
                view_distance[3] += 1
                break
            else:
                view_distance[3] += 1
        
        
        for dist in view_distance:
            scenic_score *= dist
                
        if scenic_score > max_scenic_score:
            max_scenic_score = scenic_score
                
        
print(max_scenic_score)