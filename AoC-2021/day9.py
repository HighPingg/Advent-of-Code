def day9_part1():
    with open("day9_data.txt") as f:
        heatMap = f.read().splitlines()
    
    finalSum = 0

    for i in range(len(heatMap)):
        for j in range(len(heatMap[i])):
            
            thisHeight = int(heatMap[i][j])

            # Check char above if we're not at top edge. If thisHeight is not
            # less than the one on top, then we can continue.
            if i != 0:
                if int(heatMap[i - 1][j]) <= thisHeight:
                    continue

            # Check char below if we're not at top bottom edge. If thisHeight is not
            # less than the one on bottom, then we can continue.
            if i != len(heatMap) - 1:
                if int(heatMap[i + 1][j]) <= thisHeight:
                    continue
            
            # Check char left if we're not at left edge. If thisHeight is not
            # less than the one on left, then we can continue.
            if j != 0:
                if int(heatMap[i][j - 1]) <= thisHeight:
                    continue
            
            # Check char left if we're not at left edge. If thisHeight is not
            # less than the one on left, then we can continue.
            if j != len(heatMap[i]) - 1:
                if int(heatMap[i][j + 1]) <= thisHeight:
                    continue
            
            finalSum += thisHeight + 1

    print(finalSum)

def day9_part2():
    with open("day9_data.txt") as f:
        lines = f.readlines()

    # read in the height map
    hmap = [[int(y) for y in x.strip()] for x in lines]

    # add 9's around the edges of the height map; simplifies further processing
    # padding of the top and left sides are not stricly needed
    # if loops start at row/col = 0/0 since [-1] contains 9
    # add 9 to the beginning and end of each row
    for i in range(len(hmap)):
        hmap[i].append(9)
        hmap[i].insert(0, 9)

    # add 9-rows to the top and bottom of the height map
    nines = [9] * (len(hmap[0]))
    hmap.append(nines)
    hmap.insert(0, nines)

    # recursive fill algorithm
    # fill with 9s and count the filled-in 9s
    def fill_hmap(row, col, c):
        if hmap[row][col] != 9:
            c += 1 # count the number of filled-in 9s
            hmap[row][col] = 9 # fill
            c = fill_hmap(row, col + 1, c)
            c = fill_hmap(row, col - 1, c)
            c = fill_hmap(row + 1, col, c)
            c = fill_hmap(row - 1, col, c)
        return c

    basins = []
    for row in range(1, len(hmap) - 1):
        for col in range(1, len(hmap[0]) - 1):
            b = fill_hmap(row, col, 0)
            if b != 0: # size of the basin, only save non-zero
                basins.append(b)

    basins.sort()
    print(f"Part 2: 3 largest basins multiplied = {basins[-1] * basins[-2] * basins[-3]}")
