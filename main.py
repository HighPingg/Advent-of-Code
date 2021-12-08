def day8_part1():
    with open("day8_data.txt") as f:
        data = list(map(lambda x: list(map(lambda x: x.strip().split(" "), x.split("|"))), f.read().splitlines()))
    
    count = 0
    unique_digits = [2, 4, 3, 7]    # Segment counts for 7 segment displays 1, 4, 7, 8
    for line in data:
        for output in line[1]:
            if len(output) in unique_digits:
                count += 1

    print(count)

def day8_part2():
    with open("day8_data.txt") as f:
        data = list(map(lambda x: list(map(lambda x: x.strip().split(" "), x.split("|"))), f.read().splitlines()))
    
    unique_digits = [2, 4, 3, 7]    # Segment counts for 7 segment displays 1, 4, 7, 8

    for line in data:

        

        for 

day8_part1()