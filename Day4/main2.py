def check(matrix:list, positions:tuple[int, int]) -> dict:
    dict = {'up': check_up(matrix, positions),
            'down': check_down(matrix, positions),
            'left': check_left(matrix, positions),
            'right': check_right(matrix, positions),
            'topleft': check_topleft(matrix, positions),
            'botleft': check_botleft(matrix, positions),
            'botright': check_botright(matrix, positions),
            'topright': check_topright(matrix, positions)}
    return dict

def check_diag(matrix, positions:tuple[int, int]) -> dict:
    dict = {'topleft': check_topleft(matrix, positions),
            'botleft': check_botleft(matrix, positions),
            'botright': check_botright(matrix, positions),
            'topright': check_topright(matrix, positions)}
    return dict

def check_up(matrix, positions):
    x = positions[0]
    y = positions[1]
    if x == 0:
        return None
    return matrix[x-1][y]

def check_topleft(matrix, positions):
    x = positions[0]
    y = positions[1]
    if x == 0 or y == 0:
        return None
    return matrix[x-1][y-1]

def check_left(matrix, positions):
    x = positions[0]
    y = positions[1]
    if y == 0:
        return None
    return matrix[x][y-1]

def check_botleft(matrix, positions):
    x = positions[0]
    y = positions[1]
    if x == len(matrix)-1 or y == 0:
        return None
    return matrix[x+1][y-1]

def check_down(matrix, positions):
    x = positions[0]
    y = positions[1]
    if x == len(matrix)-1:
        return None
    return matrix[x+1][y]

def check_botright(matrix, positions):
    x = positions[0]
    y = positions[1]
    if x == len(matrix)-1 or y == len(matrix[0])-1:
        return None
    return matrix[x+1][y+1]

def check_right(matrix, positions):
    x = positions[0]
    y = positions[1]
    if y == len(matrix)-1:
        return None
    return matrix[x][y+1]

def check_topright(matrix, positions):
    x = positions[0]
    y = positions[1]
    if x == 0 or y == len(matrix)-1:
        return None
    return matrix[x-1][y+1]

with open('input.txt', 'r') as file:
    matrix = [[char for char in line.strip()] for line in file]

    #results
    xmas = 0
    mas = 0

    for i, row in enumerate(matrix):
        for j, char in enumerate(row):
            if char == 'X':
                around = check(matrix, (i, j))
                for key, value in around.items():
                    if key == 'up' and value == 'M':
                        if check_up(matrix, (i-1, j)) == 'A':
                            if check_up(matrix, (i-2, j)) == 'S':
                                xmas += 1
                    if key == 'topleft' and value == 'M':
                        if check_topleft(matrix, (i-1, j-1)) == 'A':
                            if check_topleft(matrix, (i-2, j-2)) == 'S':
                                xmas += 1                                
                    if key == 'left' and value == 'M':
                        if check_left(matrix, (i, j-1)) == 'A':
                            if check_left(matrix, (i, j-2)) == 'S':
                                xmas += 1
                    if key == 'botleft' and value == 'M':
                        if check_botleft(matrix, (i+1, j-1)) == 'A':
                            if check_botleft(matrix, (i+2, j-2)) == 'S':
                                xmas += 1
                    if key == 'down' and value == 'M':
                        if check_down(matrix, (i+1, j)) == 'A':
                            if check_down(matrix, (i+2, j)) == 'S':
                                xmas += 1
                    if key == 'botright' and value == 'M':
                        if check_botright(matrix, (i+1, j+1)) == 'A':
                            if check_botright(matrix, (i+2, j+2)) == 'S':
                                xmas += 1
                    if key == 'right' and value == 'M':
                        if check_right(matrix, (i, j+1)) == 'A':
                            if check_right(matrix, (i, j+2)) == 'S':
                                xmas += 1
                    if key == 'topright' and value == 'M':
                        if check_topright(matrix, (i-1, j+1)) == 'A':
                            if check_topright(matrix, (i-2, j+2)) == 'S':
                                xmas += 1
                
            if char == 'A':
                diags = check_diag(matrix, (i, j))
                if ((diags['topleft'] == 'M' and diags['botright'] == 'S') or (diags['topleft'] == 'S' and diags['botright'] == 'M')) and ((diags['botleft'] == 'M' and diags['topright'] == 'S') or (diags['botleft'] == 'S' and diags['topright'] == 'M')):
                    mas += 1
                
    


    print(xmas)
    print(mas)

