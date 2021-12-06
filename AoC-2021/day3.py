from copy import deepcopy

def day3_part1():
    data = open("day3_data.txt").read().split("\n")

    rates = [0 for _ in range(len(data[0]))]

    for line in data:
        for i in range(len(line)):
            if line[i] == '1':
                rates[i] += 1
            else:
                rates[i] -= 1

    epsilon = ""
    gamma = ""
    for bit in rates:
        if bit > 0:
            epsilon += "0"
            gamma += "1"
        else:
            epsilon += "1"
            gamma += "0"
    
    print(int(epsilon, 2) * int(gamma, 2))

def day3_part2():
    o2_rating = open("day3_data.txt").read().split("\n")
    co2_rating = deepcopy(o2_rating)

    for i in range(len(o2_rating[0])):
        # Get most common bit pos/0 = 1
        mostCommon = 0
        for line in o2_rating:
            if line[i] == '1':
                mostCommon += 1
            else:
                mostCommon -= 1
        
        if mostCommon >= 0:
            mostCommon = '1'
        else:
            mostCommon = '0'

        o2_rating = list(filter(lambda x: x[i] == mostCommon, o2_rating))

    for i in range(len(co2_rating[0])):
        # Get most common bit +/0 = 1
        mostCommon = 0
        for line in co2_rating:
            if line[i] == '1':
                mostCommon += 1
            else:
                mostCommon -= 1
        
        if mostCommon >= 0:
            mostCommon = '1'
        else:
            mostCommon = '0'

        co2_rating = list(filter(lambda x: x[i] != mostCommon, co2_rating))

        if(len(co2_rating) == 1):
            break

    print(int(o2_rating[0], 2) * int(co2_rating[0], 2))
