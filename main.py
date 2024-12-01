#didnt know if there was already a python builtin that did this, so just quickly wrote own
def find_distance(x, y):
    if x == y:
        return 0
    return max((x, y)) - min((x, y))

with open('input.txt', 'r') as input_file:
    left = []
    right = []
    distance = []
    similarities = []

    for line in input_file:
        splitline = line.split()
        left.append(splitline[0])
        right.append(splitline[1])
    
    left.sort()
    right.sort()

    for i in range(len(left)):
        #a little hard to read, but effective
        distance.append(find_distance(int(left[i]), int(right[i])))
        
    #dictionary comprehension, counts how many times number in left list appears in right list
    counts = {i:right.count(i) for i in left}

    for num in left:
        similarities.append(int(num) * counts[num])


    print(f'sum distance: {sum(distance)}')
    print(f'sum similarities: {sum(similarities)}')
