# Задача 4: Поиск уникальных элементов в списке. Напишите программу, которая создает новый список, содержащий только уникальные элементы из исходного списка.

def create_uniq_list(ml):
    return set(ml)


main_list = list("Hello world!")
second_list = create_uniq_list(main_list)
print(second_list)