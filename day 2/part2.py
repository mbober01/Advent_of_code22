# A rock
# B paper
# C scissors


points = {
    "A": 1,
    "B": 2,
    "C": 3
}
outcomes = {
    "Z": 6,
    "Y": 3,
    "X": 0
}
win_scenarios = {
    "A": "B",
    "B": "C",
    "C": "A"
}

lose_scenarios = {
    "A": "C",
    "B": "A",
    "C": "B"
}

with open("day 2/data.txt", 'r') as file:
    sum_of_points = 0
    player = ""
    lines = file.readlines()
    for line in lines:
        round_points = 0
        strats = line.rsplit()
        opponnent = strats[0]
        outcome = strats[1]
        if outcome == "Z":
            player = win_scenarios[opponnent]
        elif outcome == "Y":
            player = opponnent
        else:
            player = lose_scenarios[opponnent]
        round_points = points[player] + outcomes[outcome]
        sum_of_points += round_points

print(sum_of_points)
