def day11_part1():
    with open("day11_data.txt") as f:
        data = f.read().splitlines()

        for line in range(len(data)):
            split = []

            for i in data[line]:
                split.append(int(i))
            
            data[line] = split

    countpop = 0

    def popOcto(i, j):

        nonlocal countpop
        countpop += 1

        # Resets the element. Sets to -1000 so we dont pop a second time today.
        data[i][j] = -1000

        # Add 1 to neighbors. If they surpass 9, then we can pop them.
        if i != 0 and j != 0:

            data[i - 1][j - 1] += 1
            if data[i - 1][j - 1] > 9:
                popOcto(i - 1, j - 1)

        if i != 0:
            
            data[i - 1][j] += 1
            if data[i - 1][j] > 9:
                popOcto(i - 1, j)
        
        if i != 0 and j != len(data[i]) - 1:
            
            data[i - 1][j + 1] += 1
            if data[i - 1][j + 1] > 9:
                popOcto(i - 1, j + 1)

        if j != len(data[i]) - 1:
            
            data[i][j + 1] += 1
            if data[i][j + 1] > 9:
                popOcto(i, j + 1)

        if i != len(data) - 1 and j != len(data[i]) - 1:

            data[i + 1][j + 1] += 1
            if data[i + 1][j + 1] > 9:
                popOcto(i + 1, j + 1)
            
        if i != len(data) - 1:
            
            data[i + 1][j] += 1
            if data[i + 1][j] > 9:
                popOcto(i + 1, j)

        if i != len(data) - 1 and j != 0:
            
            data[i + 1][j - 1] += 1
            if data[i + 1][j - 1] > 9:
                popOcto(i + 1, j - 1)
            
        if j != 0:
            
            data[i][j - 1] += 1
            if data[i][j - 1] > 9:
                popOcto(i, j - 1)

    for step in range(100):
        
        # Increment all
        for i in range(len(data)):
            for j in range(len(data[i])):
                data[i][j] += 1
            
        for i in range(len(data)):
            for j in range(len(data[i])):
                
                # Check if octopus popped
                if data[i][j] > 9:
                    popOcto(i, j)
        
        # Resets all negative nums to 0
        for i in range(len(data)):
            for j in range(len(data[i])):
                if data[i][j] < 0:
                    data[i][j] = 0
    
    print(countpop)

def day11_part2():
    with open("day11_data.txt") as f:
        data = f.read().splitlines()

        for line in range(len(data)):
            split = []

            for i in data[line]:
                split.append(int(i))
            
            data[line] = split

    def popOcto(i, j):

        # Resets the element. Sets to -1000 so we dont pop a second time today.
        data[i][j] = -1000

        # Add 1 to neighbors. If they surpass 9, then we can pop them.
        if i != 0 and j != 0:

            data[i - 1][j - 1] += 1
            if data[i - 1][j - 1] > 9:
                popOcto(i - 1, j - 1)

        if i != 0:
            
            data[i - 1][j] += 1
            if data[i - 1][j] > 9:
                popOcto(i - 1, j)
        
        if i != 0 and j != len(data[i]) - 1:
            
            data[i - 1][j + 1] += 1
            if data[i - 1][j + 1] > 9:
                popOcto(i - 1, j + 1)

        if j != len(data[i]) - 1:
            
            data[i][j + 1] += 1
            if data[i][j + 1] > 9:
                popOcto(i, j + 1)

        if i != len(data) - 1 and j != len(data[i]) - 1:

            data[i + 1][j + 1] += 1
            if data[i + 1][j + 1] > 9:
                popOcto(i + 1, j + 1)
            
        if i != len(data) - 1:
            
            data[i + 1][j] += 1
            if data[i + 1][j] > 9:
                popOcto(i + 1, j)

        if i != len(data) - 1 and j != 0:
            
            data[i + 1][j - 1] += 1
            if data[i + 1][j - 1] > 9:
                popOcto(i + 1, j - 1)
            
        if j != 0:
            
            data[i][j - 1] += 1
            if data[i][j - 1] > 9:
                popOcto(i, j - 1)

    def allzeros():
        for line in data:
            for cell in line:
                if cell != 0:
                    return False
        return True

    stepcount = 0
    while not allzeros():
        
        stepcount += 1

        # Increment all
        for i in range(len(data)):
            for j in range(len(data[i])):
                data[i][j] += 1
            
        for i in range(len(data)):
            for j in range(len(data[i])):
                
                # Check if octopus popped
                if data[i][j] > 9:
                    popOcto(i, j)
        
        # Resets all negative nums to 0
        for i in range(len(data)):
            for j in range(len(data[i])):
                if data[i][j] < 0:
                    data[i][j] = 0
    
    print(stepcount)
