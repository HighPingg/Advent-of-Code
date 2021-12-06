def day2_part1():
    data = open("day2_data.txt").read().split("\n")
    data = list(map(lambda x: x.split(" "), data))

    horizontal_pos = 0
    vertical_pos = 0


    for pair in data:
        if(pair[0] == 'forward'):
            horizontal_pos += int(pair[1])
        elif(pair[0] == 'up'):
            vertical_pos -= int(pair[1])
        elif(pair[0] == 'down'):
            vertical_pos += int(pair[1])
    
    print(horizontal_pos * vertical_pos)

def day2_part2():
    data = open("day2_data.txt").read().split("\n")
    data = list(map(lambda x: x.split(" "), data))

    horizontal_pos = 0
    vertical_pos = 0
    aim = 0

    for pair in data:
        if(pair[0] == 'forward'):
            X = int(pair[1])
            horizontal_pos += X
            vertical_pos += X * aim

        elif(pair[0] == 'up'):
            X = int(pair[1])
            aim -= X

        elif(pair[0] == 'down'):
            X = int(pair[1])
            aim += X
    
    print(horizontal_pos * vertical_pos)
