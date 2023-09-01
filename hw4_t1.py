# Фибоначчи через рекурсию: Напишите рекурсивную функцию для вычисления числа Фибоначчи с индексом n. 
# Напоминаю, что последовательность Фибоначчи определяется как: F(0) = 0, F(1) = 1 и F(n) = F(n-1) + F(n-2) для n > 1.

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return (fibonacci(n - 1) + fibonacci(n - 2))



num = int(input("Input num: "))

print(f"F({num}) = {fibonacci(num)}")