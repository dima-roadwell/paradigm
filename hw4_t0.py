# Рекурсивная сумма: Напишите рекурсивную функцию, которая вычисляет сумму всех чисел от 1 до n. Например, для n = 5 результат должен быть 1 + 2 + 3 + 4 + 5 = 15.
# Факториал: Напишите рекурсивную функцию для вычисления факториала числа n. Факториал числа n обозначается как n! и равен произведению всех положительных целых чисел от 1 до n.

def sum_nums(n):
    if n == 0:
        return 0
    else:
        n += sum_nums(n - 1)
        return n
    
def calculate_fact(n):
    if n == 1:
        return 1
    else:
        n *= calculate_fact(n - 1)
        return n




num = int(input("Input num: "))

sum = sum_nums(num)
fact = calculate_fact(num)

print(f"Sum: {sum}")
print(f"Factorial: {fact}")