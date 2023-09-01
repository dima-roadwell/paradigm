# Замыкание: Создайте функцию, которая принимает некоторое число n и возвращает функцию, которая прибавляет n к своему аргументу. 
# Продемонстрируйте использование этой функции-замыкания.

def outer_func(x):
    def inner_func(y):
        return x + y
    return inner_func

num = outer_func(int(input("Input num: ")))
res = num(5)

print(res)