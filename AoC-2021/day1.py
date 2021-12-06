def day1_part1():
    data = open("day1_data.txt", mode = 'r').read().split("\n")

    count = 0
    for i in range(1, len(data)):
        if int(data[i]) > int(data[i - 1]):
            count += 1

    print(count)

def day1_part2():
    with open(f'day1_data.txt', 'r') as f:
        numbers = [int(s) for s in f.read().splitlines()]

    def part1(numbers):
        return sum([x < y for x, y in zip(numbers, numbers[1:])])


    def part2(numbers):
        return [x+y+z for x, y, z in zip(numbers, numbers[1:], numbers[2:])]

    print(part1(part2(numbers)))
