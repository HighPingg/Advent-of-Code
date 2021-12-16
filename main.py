from collections import defaultdict

def day12_part1():
    with open("day12_data.txt") as f:
        data = f.read().splitlines()

        adjacent = defaultdict(list)

        for line in data:

            left, right = line.split("-")

            adjacent[left].append(right)
            adjacent[right].append(left)
    
    def dfs(currentVert: str, found):

        if currentVert == "end":
            return 1
        
        if currentVert.islower() and currentVert in found:
            return 0
        
        found = found | {currentVert}

        total = 0
        for vert in adjacent[currentVert]:
            total += dfs(vert, found)
        
        return total
    
    print(dfs("start", set()))

def day12_part2():
    with open("adad.txt") as f:
        data = f.read().splitlines()

        adjacent = defaultdict(list)

        for line in data:

            left, right = line.split("-")

            adjacent[left].append(right)
            adjacent[right].append(left)
    
    def dfs(currentVert: str, found):
        print(currentVert, found)
        if currentVert == "end":
            return 1

        if len(list(filter(lambda x: x == currentVert, found))) == 2:
            return 0

        total = 0
        for vert in adjacent[currentVert]:
            if vert == "start":
                continue

            found.append(vert)

            total += dfs(vert, found)
        
            found.pop()

        return total
    
    print(dfs("start", []))

day12_part2()