def day10_part1():
    with open("day10_data.txt") as f:
        data = f.read().splitlines()
    
    possible_delims = [['(', '{', '<', '['], [')', '}', '>', ']']]

    total_violations = 0

    for line in data:
        stack = []

        for delim in line:
            if delim in possible_delims[0]:
                stack.append(delim)
            else:
                # If invalid
                if stack.pop() != possible_delims[0][possible_delims[1].index(delim)]:
                    if delim == ')':
                        total_violations += 3
                    elif delim == ']':
                        total_violations += 57
                    elif delim == '}':
                        total_violations += 1197
                    elif delim == '>':
                        total_violations += 25137
    
    print(total_violations)

def day10_part2():
    with open("day10_data.txt") as f:
        data = f.read().splitlines()
    
    possible_delims = [['(', '{', '<', '['], [')', '}', '>', ']']]

    total_score = []

    for line in data:
        stack = []

        corrupted = False

        for delim in line:
            if delim in possible_delims[0]:
                stack.append(delim)
            else:
                # If invalid
                if stack.pop() != possible_delims[0][possible_delims[1].index(delim)]:
                    corrupted = True
                    break
    
        if len(stack) != 0 and not corrupted:
            # Iterate through the stack and add total points
            score = 0

            for delim in stack[::-1]:
                score *= 5

                if delim == '(':
                    score += 1
                elif delim == '[':
                    score += 2
                elif delim == '{':
                    score += 3
                elif delim == '<':
                    score += 4
            
            total_score.append(score)

    total_score.sort()
    print(total_score[len(total_score) // 2])
