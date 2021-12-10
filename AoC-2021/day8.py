def day8_part1():
    with open("day8_data.txt") as f:
        data = list(map(lambda x: list(map(lambda x: x.strip().split(" "), x.split("|"))), f.read().splitlines()))
    
    count = 0
    unique_digits = [2, 4, 3, 7]    # Segment counts for 7 segment displays 1, 4, 7, 8
    for line in data:
        for output in line[1]:
            if len(output) in unique_digits:
                count += 1

    print(count)

def day8_part2():
    with open("day8_data.txt") as f:
        data = list(map(lambda x: list(map(lambda x: x.strip().split(" "), x.split("|"))), f.read().splitlines()))

    final_sum = 0

    for line in data:
        
        digits_found = [0 for _ in range(10)]

        # Go through first and find digits 1, 4, 7, 8
        for digit in line[0]:
            if len(digit) == 2:
                digits_found[1] = digit
            elif len(digit) == 4:
                digits_found[4] = digit
            elif len(digit) == 3:
                digits_found[7] = digit
            elif len(digit) == 7:
                digits_found[8] = digit
        
        # We can now deal with digits 2, 3, and 5, which all have 5 segments. We can store them in an intermediary array
        five_segs = []
        for digit in line[0]:
            if len(digit) == 5:
                five_segs.append(digit)
        
        # To find 3, we can subtract 2,3,5 from 1. The digit with the smallest length must be 3.
        three_index = 0
        three_len = 5
        for digit in range(len(five_segs)):
            diff = str_diff(five_segs[digit], digits_found[1])
            if len(diff) < three_len:
                three_len = len(diff)
                three_index = digit

        # Sets the third digit and removes 3 from the list
        digits_found[3] = five_segs[three_index]
        five_segs.pop(three_index)
        
        # We now can find 2 and 5. Subtract digit from 4 and the one with less is 5
        if len(str_diff(five_segs[0], digits_found[4])) < len(str_diff(five_segs[1], digits_found[4])):
            
            # five_segs[0] must be 5
            digits_found[5] = five_segs[0]
            digits_found[2] = five_segs[1]
        else:
            digits_found[2] = five_segs[0]
            digits_found[5] = five_segs[1]
        
        # We can now process 0, 6, and 9.
        six_segs = []
        for digit in line[0]:
            if len(digit) == 6:
                six_segs.append(digit)

        # We can now subtract the digits with six segments from 1. The one with the greatest length must be
        # 6.
        six_index = 0
        six_len = 0
        for digit in range(len(six_segs)):
            diff = str_diff(six_segs[digit], digits_found[1])
            if len(diff) > six_len:
                six_len = len(diff)
                six_index = digit
        
        # Sets the third digit and removes 3 from the list
        digits_found[6] = six_segs[six_index]
        six_segs.pop(six_index)

        # We now can find 0 and 9. Subtract digit from 4 and the one with less is 9
        if len(str_diff(six_segs[0], digits_found[4])) < len(str_diff(six_segs[1], digits_found[4])):
            
            # six_segs[0] must be 9
            digits_found[9] = six_segs[0]
            digits_found[0] = six_segs[1]
        else:
            digits_found[0] = six_segs[0]
            digits_found[9] = six_segs[1]

        # We can now parse the digits left of the delimiter.
        converted_str = ""
        for digit in line[1]:
            for num in range(len(digits_found)):
                if str_eq(digit, digits_found[num]):
                    converted_str += str(num)

        final_sum += int(converted_str)
    
    print(final_sum)


def str_diff(str1, str2):
    result = ""

    for char in str1:
        if char not in str2:
            result += char
    
    return result

def str_eq(str1, str2):

    if len(str1) != len(str2):
        return False

    for char in str1:
        if char not in str2:
            return False
    
    return True
