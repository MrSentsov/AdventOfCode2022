# Parsing the data as sting values
with open('day1.in') as file:
    data = [i for i in file.read().strip().split("\n")]

    first_place = 0
    second_place = 0
    third_place = 0
    calorie_count = 0
# Looping through the data
    for item in data:
        if item == '':
            calorie_count = 0
        else:
            num = int(item)
            calorie_count = calorie_count + num
        if calorie_count > first_place:
            first_place = calorie_count
        elif calorie_count > second_place:
            second_place = calorie_count
        elif calorie_count > third_place:
            third_place = calorie_count

    print('Part 1 answer:', first_place)
    print('Part 2 answer:', first_place+second_place+third_place)