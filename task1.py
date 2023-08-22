# Задача 2: Поиск наименьшего числа в списке. Напишите программу, которая находит наименьшее число в заданном списке с помощью цикла.

def find_min_num(l):
    min_num = l[0]
    for i in range(len(l)):
        if min_num > l[i]:
            min_num = l[i]
    return min_num

li = [14, 21, 53, 10, 37]
print(find_min_num(li))