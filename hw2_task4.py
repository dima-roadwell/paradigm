# В целом, понимаю, как проходить по лабиринту, но в некоторых случаях выдает исключения в связи с выходом за границы массива. Прошу понять и простить :)

from random import randint

def create_labyrinth(m, n, start_point, end_point):
    labyrinth = [[-1] * m for i in range(n)]
    # labyrinth = [[0, 0, 1], [1, 0, 0], [1, 1, 0]]
    current_point = start_point
    
    for i in range(m):
        for j in range(n):
            rnd = randint(0, 1)
            labyrinth[i][j] = rnd

    available_points = []

    next_point = [current_point[0], current_point[1] + 1]
    prev_point = []
    
    counter = 0
    
    while counter < 4 and current_point != end_point:
        if next_point[1] >= len(labyrinth[0]) or labyrinth[next_point[0]][next_point[1]] == 1:
            next_point = [current_point[0] + 1, current_point[1]]

            counter += 1
        elif next_point[1] > 0 and labyrinth[next_point[0]][next_point[1]] == 1:
            next_point[current_point[0], current_point[1] - 1]

            counter += 1  
        elif next_point[0] > 0 and labyrinth[next_point[0]][next_point[1]] == 1:
            next_point[current_point[0] - 1, current_point[1]] 

            counter += 1
        else:
            available_points.append([next_point[0], next_point[1]])

            prev_point = current_point
            current_point = next_point
            next_point = [current_point[0], current_point[1] + 1]

            counter = 0


    print(available_points)

    
    
        



create_labyrinth(3, 3, [0, 0], [2, 2])