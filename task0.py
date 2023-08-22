# Задача 1: Подсчет суммы четных чисел от 1 до N. Напишите программу, используя цикл, которая находит сумму всех четных чисел в диапазоне от 1 до заданного числа N.

def sum(n):
    total = 0
    for i in range(0, n, 2):
        total += i
    return total

num = int(input("Input num: "))
print(sum(num))