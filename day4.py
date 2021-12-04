def day4_part1():
    file = open("day4_data.txt", 'r')

    # Get list of data
    nums = file.readline().split(',')

    # Discard empty space
    file.readline()

    # Read the rest of the file
    data = file.read().split('\n')
    
    # Create boards out of data
    boards = [[]]
    count = 0
    for line in data:
        if line == '':
            count += 1
            boards.append([])
        else:
            boards[count].append(line)
    
    # We need to now split each line up by spaces.
    for i in range(len(boards)):
        for j in range(5):
            boards[i][j] = boards[i][j].split(" ")

            while boards[i][j].__contains__(""):
                boards[i][j].remove("")

    for num in nums:
        for board in range(len(boards)):
            for row in range(len(boards[board])):
                while boards[board][row].__contains__(num):
                    index = boards[board][row].index(num)
                    boards[board][row][index] = -1
        
            # If this board is a winner, go through all elems and sum up all elems not -1.
            if is_winner(boards[board]):
                summ = 0

                for row in boards[board]:
                    summ += sum(map(lambda x: int(x), filter(lambda x: x != -1, row)))
                
                print(summ * int(num))
                return

def day4_part2():
    file = open("day4_data.txt", 'r')

    # Get list of data
    nums = file.readline().split(',')

    # Discard empty space
    file.readline()

    # Read the rest of the file
    data = file.read().split('\n')
    
    # Create boards out of data
    boards = [[]]
    count = 0
    for line in data:
        if line == '':
            count += 1
            boards.append([])
        else:
            boards[count].append(line)
    
    # We need to now split each line up by spaces.
    for i in range(len(boards)):
        for j in range(5):
            boards[i][j] = boards[i][j].split(" ")

            while boards[i][j].__contains__(""):
                boards[i][j].remove("")

    winners = []
    finalsumm = 0

    for num in nums:
        for board in range(len(boards)):
            for row in range(len(boards[board])):
                while boards[board][row].__contains__(num):
                    index = boards[board][row].index(num)
                    boards[board][row][index] = -1
        
            # If this board is a winner, go through all elems and sum up all elems not -1.
            if is_winner(boards[board]) and not winners.__contains__(board):
                summ = 0

                for row in boards[board]:
                    summ += sum(map(lambda x: int(x), filter(lambda x: x != -1, row)))
                
                winners.append(board)
                finalsumm = summ * int(num)
                
    print(finalsumm)

def is_winner(lst):
    # Check row for winner
    for row in lst:
        if row == [-1, -1, -1, -1, -1]:
            return True
    
    # Check column for winner
    for i in range(len(lst)):
        colmatch = True
        for j in range(len(lst[i])):
            if lst[j][i] != -1:
                colmatch = False
        if colmatch:
            return True
    
    return False
