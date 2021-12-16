from copy import deepcopy

def day13_part1():
    with open("day13_data.txt") as f:
        data = f.read().split("\n\n")

        data[0] = data[0].splitlines()
        data[1] = data[1].splitlines()

        # Generate empty grid
        max_x = 0
        max_y = 0

        for point in data[0]:
            x, y = point.split(",")
            max_x = max(max_x, int(x))
            max_y = max(max_y, int(y))

        max_x = max_x + 1 if max_x % 2 == 1 else max_x
        max_y = max_y + 1 if max_y % 2 == 1 else max_y

        grid = [['.' for _ in range(max_x + 1)] for _ in range(max_y + 2)]

        # Fill in #s
        for point in data[0]:
            x, y = map(lambda x: int(x), point.split(","))
            grid[y][x] = '#'

    # Take the first instruction
    if 'y' in data[1][0]:
        # Partition the array into 2.
        # 1. From y = 0 to the partition + 1
        # 2. From y = partition to the end of the array

        partition = int(data[1][0].split("=")[1])
        partition1 = []
        partition2 = []

        for line in range(partition):
            partition1.append(deepcopy(grid[line]))

        for line in range(partition + 1, len(grid)):
            partition2.insert(0, deepcopy(grid[line]))

        newgrid = [['.' for _ in range(len(partition1[0]))] for _ in range(len(partition1))]

        for y in range(len(partition1)):
            for x in range(len(partition1[y])):
                if partition1[y][x] == '#' or partition2[y][x] == '#':
                    newgrid[y][x] = '#'

        # Sets the grid to the new grid
        grid = newgrid
    
    else:
        # Partition the array into 2.
        # 1. From x = 0 to the partition
        # 2. From x = partition + 1 to the end of the array

        partition = int(data[1][0].split("=")[1])
        partition1 = []
        partition2 = []

        for line in grid:
            partition1.append(deepcopy(line[:partition]))
            partition2.append(deepcopy(line[len(line) - 1: partition : -1]))

        newgrid = [['.' for _ in range(len(partition1[0]))] for _ in range(len(partition1))]

        for y in range(len(partition1)):
            for x in range(len(partition1[y])):
                if partition1[y][x] == '#' or partition2[y][x] == '#':
                    newgrid[y][x] = '#'
        
        grid = newgrid

    print(sum(list(map(lambda x: x.count('#'), grid))))

def day13_part2():
    with open("day13_data.txt") as f:
        data = f.read().split("\n\n")

        data[0] = data[0].splitlines()
        data[1] = data[1].splitlines()

        # Generate empty grid
        max_x = 0
        max_y = 0

        for point in data[0]:
            x, y = point.split(",")
            max_x = max(max_x, int(x))
            max_y = max(max_y, int(y))

        grid = [['.' for _ in range(max_x + 1)] for _ in range(max_y + 2)]

        # Fill in #s
        for point in data[0]:
            x, y = map(lambda x: int(x), point.split(","))
            grid[y][x] = '#'

    # Take the first instruction
    for instr in data[1]:
        print(len(grid[0]), len(grid))
        if 'y' in instr:
            # Partition the array into 2.
            # 1. From y = 0 to the partition + 1
            # 2. From y = partition to the end of the array

            partition = int(instr.split("=")[1])
            partition1 = []
            partition2 = []

            for line in range(partition):
                partition1.append(deepcopy(grid[line]))
            print(partition + 1, len(grid))
            for line in range(partition + 1, len(grid)):
                partition2.insert(0, deepcopy(grid[line]))

            newgrid = [['.' for _ in range(len(partition1[0]))] for _ in range(len(partition1))]
            
            for y in range(len(partition1)):
                for x in range(len(partition1[y])):
                    if partition1[y][x] == '#' or partition2[y][x] == '#':
                        newgrid[y][x] = '#'

            # Sets the grid to the new grid
            grid = newgrid
        
        else:
            # Partition the array into 2.
            # 1. From x = 0 to the partition
            # 2. From x = partition + 1 to the end of the array

            partition = int(instr.split("=")[1])
            partition1 = []
            partition2 = []

            for line in grid:
                partition1.append(deepcopy(line[:partition]))
                partition2.append(deepcopy(line[len(line) - 1: partition : -1]))

            newgrid = [['.' for _ in range(len(partition1[0]))] for _ in range(len(partition1))]

            for y in range(len(partition1)):
                for x in range(len(partition1[y])):
                    if partition1[y][x] == '#' or partition2[y][x] == '#':
                        newgrid[y][x] = '#'
            
            grid = newgrid
    
    for i in grid:
        print(i)

day13_part2()