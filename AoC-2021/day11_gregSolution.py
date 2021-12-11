lines = []
with open('in.txt') as f:
    for line in f:
        lines.append(line.strip())

nums = [[int(x) for x in list(line)] for line in lines]

def valid(r, c):
    return r >= 0 and r < 10 and c >= 0 and c < 10

flashes = 0
for step in range(100000000):
    grid = [[False for _ in line] for line in nums]
    new_nums = [[x+1 for x in line] for line in nums]
    found_one = True
    local_flash = 0
    while found_one:
        found_one = False
        for r in range(10):
            for c in range(10):
                if new_nums[r][c] >= 10 and not grid[r][c]:
                    flashes += 1
                    local_flash += 1
                    grid[r][c] = True
                    new_nums[r][c] = 0
                    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]:
                        if valid(r+dr, c+dc) and not grid[r+dr][c+dc]:
                            new_nums[r+dr][c+dc] += 1
                            found_one = True

    if local_flash == 100:
        print(step+1)
        break
    nums = new_nums 