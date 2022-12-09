# A  X rock
# B  Y paper
# C  Z scissors

points = {
    "X":1,
    "Y":2,
    "Z":3
}

outcomes = {
    "win":6,
    "draw":3,
    "lose":0
}

with open("day 2/data.txt", 'r') as file:
    sum_of_points = 0
    lines = file.readlines()
    for line in lines:
        round_points = 0
        strats = line.rsplit()
        opponent = strats[0]
        player = strats[1]
        if opponent == "A":
            if player == "X":
                outcome = "draw"
            elif player == "Y":
                outcome = "win"
            else:
                outcome = "lose"
        elif opponent == "B":
            if player == "X":
                outcome = "lose"
            elif player == "Y":
                outcome = "draw"
            else:
                outcome = "win"
        else:
            if player == "X":
                outcome = "win"
            elif player == "Y":
                outcome = "lose"
            else:
                outcome = "draw"


        round_points = outcomes[outcome] + points[player]
        sum_of_points += round_points

print(sum_of_points)