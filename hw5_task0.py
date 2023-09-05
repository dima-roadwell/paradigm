# Задача 1: Напишите программу, которая находит все простые числа в заданном диапазоне.

def check_prime_number(start_n, end_n):
    prime_numbers = []

    for i in range(start_n, end_n + 1):
        if i > 1:
            if i == 2:
                prime_numbers.append(i)
            else:
                for j in range(2, i):
                    if i % j == 0:
                        break
                    if j == i - 1 and i - 1 % j != 0:
                        prime_numbers.append(i)
                
    print(prime_numbers)

start_num = int(input("Input start num: "))
end_num = int(input("Input end num: "))

check_prime_number(start_num, end_num)