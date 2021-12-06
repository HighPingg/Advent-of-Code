def day6_part1():
    with open("day6_data.txt") as f:
        fish = list(map(lambda x: int(x), f.read().split(",")))
    
    for j in range(256):

        newFish = 0

        for i in range(len(fish)):
            if fish[i] == 0:
                fish[i] = 6
                newFish += 1
            else:
                fish[i] -= 1

        fish += [8 for _ in range(newFish)]
    
    print(len(fish))

def day6_part2():
    with open("day6_data.txt") as f:
        fish = f.read().split(",")

    # We will create an array of index of size 9 where each index is the amount of days it has left to give birth.
    fish = [0,
            len(list(filter(lambda x: x == '1', fish))),
            len(list(filter(lambda x: x == '2', fish))),
            len(list(filter(lambda x: x == '3', fish))),
            len(list(filter(lambda x: x == '4', fish))),
            len(list(filter(lambda x: x == '5', fish))),
            0, 0, 0]

    for _ in range(256):

        newfish = fish[0]

        for i in range(len(fish) - 1):
            fish[i] = fish[i + 1]
        
        fish[8] = newfish
        fish[6] += newfish

    print(sum(fish))
