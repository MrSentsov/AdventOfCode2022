# Get the data into an iterative list
with open("day2.in") as file:
    rounds = [i for i in file.read().strip().split("\n")]

# All possible outcomes
# TODO: Read more about Python dictionaries
outcomes = {
    "A X":4, "A Y":8, "A Z":3,
    "B X":1, "B Y":5, "B Z":9,
    "C X":7, "C Y":2, "C Z":6
}

desired_outcomes = {
    "A X":3, "A Y":4, "A Z":8,
    "B X":1, "B Y":5, "B Z":9,
    "C X":2, "C Y":6, "C Z":7
}

total_points_part_1 = 0
total_points_Part_2 = 0

for round in rounds:
    total_points_part_1 += outcomes[round]
    total_points_Part_2 += desired_outcomes[round]

print('Part 1 answer:', total_points_part_1)
print('Part 2 answer:', total_points_Part_2)