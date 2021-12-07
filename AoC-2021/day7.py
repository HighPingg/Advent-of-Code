def day7_part1():
    with open("day7_data.txt") as f:
        positions = list(map(lambda x: int(x), f.read().split(",")))
    
    total_crabs = [0 for _ in range(max(positions) + 1)]

    # We're going to move all crabs to a position in total_crabs and find the fuel needed.
    for i in range(len(total_crabs)):
        for position in positions:
            total_crabs[i] += abs(position - i)
    
    print(min(total_crabs))

def day7_part2():
    with open("day7_data.txt") as f:
        positions = list(map(lambda x: int(x), f.read().split(",")))
    
    total_crabs = [0 for _ in range(max(positions) + 1)]

    # We're going to move all crabs to a position in total_crabs and find the fuel needed.
    for i in range(len(total_crabs)):
        for position in positions:
            # Simply add (distance + 1) * distance / 2
            total_crabs[i] += ((abs(position - i) + 1) * abs(position - i)) // 2
    
    print(min(total_crabs))
