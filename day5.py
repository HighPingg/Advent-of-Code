def day5_part1():
    data = open("day5_data.txt").read().splitlines()

    get_largest_x = 0
    get_largest_y = 0

    # Turn data into 3D list of 2 pairs
    for i in range(len(data)):
        temp = data[i].split(" -> ")

        temp[0] = list(map(lambda x: int(x), temp[0].split(",")))
        temp[1] = list(map(lambda x: int(x), temp[1].split(",")))

        data[i] = temp

        if temp[1][0] > get_largest_x:
            get_largest_x = temp[1][0]
        
        if temp[1][1] > get_largest_y:
            get_largest_y = temp[1][1]
    
    # Create our list of 0s.
    grid = [[0 for _ in range(get_largest_x + 1)] for _ in range(get_largest_y + 1)]

    for lines in data:
        # If the x values are the same, then add to the vertical position
        if lines[0][0] == lines[1][0]:

            first = min(lines[0][1], lines[1][1])
            second = max(lines[0][1], lines[1][1])

            for i in range(first, second + 1):
                grid[i][lines[0][0]] += 1
        
        # Otherwise if the y values are the same and we can iterate through x values
        elif lines[0][1] == lines[1][1]:
            
            first = min(lines[0][0], lines[1][0])
            second = max(lines[0][0], lines[1][0])

            for i in range(first, second + 1):
                grid[lines[0][1]][i] += 1

    count = 0
    for row in grid:
        for num in row:
            if num >= 2:
                count += 1

    print(count)

def day5_part2():
    data = open("day5_data.txt").read().splitlines()

    get_largest_x = 0
    get_largest_y = 0

    # Turn data into 3D list of 2 pairs
    for i in range(len(data)):
        temp = data[i].split(" -> ")

        temp[0] = list(map(lambda x: int(x), temp[0].split(",")))
        temp[1] = list(map(lambda x: int(x), temp[1].split(",")))

        data[i] = temp

        if temp[1][0] > get_largest_x:
            get_largest_x = temp[1][0]
        
        if temp[1][1] > get_largest_y:
            get_largest_y = temp[1][1]
    
    # Create our list of 0s.
    grid = [[0 for _ in range(get_largest_x + 1)] for _ in range(get_largest_y + 1)]

    for lines in data:
        # If the x values are the same, then add to the vertical position
        if lines[0][0] == lines[1][0]:

            first = min(lines[0][1], lines[1][1])
            second = max(lines[0][1], lines[1][1])

            for i in range(first, second + 1):
                grid[i][lines[0][0]] += 1
        
        # Otherwise if the y values are the same and we can iterate through x values
        elif lines[0][1] == lines[1][1]:
            
            first = min(lines[0][0], lines[1][0])
            second = max(lines[0][0], lines[1][0])

            for i in range(first, second + 1):
                grid[lines[0][1]][i] += 1

        # Else if the absolute value of their slopes is 1, then its diagonal
        elif abs((lines[1][1] - lines[0][1]) / (lines[1][0] - lines[0][0])) == 1:

            # There are 2 cases: 1. Positive slope. 
            # We want to take the lesser x value and iterate from that one.
            if (lines[1][1] - lines[0][1]) / (lines[1][0] - lines[0][0]) == 1:
                first = min(lines[0][0], lines[1][0])
                second = max(lines[0][0], lines[1][0])

                for i in range(0, second - first + 1):
                    if lines[1][0] > lines[0][0]:
                        grid[lines[0][1] + i][lines[0][0] + i] += 1
                    else:
                        grid[lines[1][1] + i][lines[1][0] + i] += 1
            
            # 2. Negative slope.
            else:
                # Find the range of numbers
                first = min(lines[0][0], lines[1][0])
                second = max(lines[0][0], lines[1][0])

                for i in range(0, second - first + 1):
                    if lines[0][0] > lines[1][0]:
                        grid[lines[0][1] + i][lines[0][0] - i] += 1
                    else:
                        grid[lines[1][1] + i][lines[1][0] - i] += 1

    count = 0
    for row in grid:
        for num in row:
            if num >= 2:
                count += 1

    print(count)
