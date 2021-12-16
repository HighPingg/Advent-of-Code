from collections import defaultdict

def day14_part1():
    with open('day14_data.txt') as f:
        template = f.readline().replace('\n', '');
        
        # Discard empty line
        f.readline()

        pairs = {}
        for line in f.read().splitlines():
            pair, x = line.split(' -> ')
            pairs[pair] = x

    for _ in range(10):
        newString = template[0]

        for i in range(1, len(template)):
            newString += pairs[template[i - 1] + template[i]] + template[i]

        template = newString
    
    counts = defaultdict(lambda: 0)
    for i in template:
        counts[i] += 1
    
    print(max(counts.values()) - min(counts.values()))

def day14_part2():
    with open('day14_data.txt') as f:
        template = f.readline().replace('\n', '')
        
        # Discard empty line
        f.readline()

        pairs = {}
        for line in f.read().splitlines():
            pair, x = line.split(' -> ')
            pairs[pair] = x

    # All possible pairs
    currentStep = defaultdict(int)
    for i in range(len(template) - 1):
        currentStep[template[i:i+2]] += 1
    # We need to add the last element since it also contributes, but isnt a pair.
    currentStep[template[-1]] += 1

    for i in range(40):
        nextStep = defaultdict(int)

        for pair, count in currentStep.items():
            if pair in pairs:
                nextStep[pair[0] + pairs[pair]] += count
                nextStep[pairs[pair] + pair[1]] += count
            else:
                nextStep[pair] += count

        currentStep = nextStep
    
    counts = defaultdict(lambda: 0)
    for pair, count in currentStep.items():
        counts[pair[0]] += count
    
    print(max(counts.values()) - min(counts.values()))

day14_part2()