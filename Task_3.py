# Реализуйте алгоритм перемешивания списка. 
# НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE, 
# максимум использование библиотеки Random для и получения случайного int


def fill_list(size: int, min_number: int, max_number: int) -> list:
    from random import randint
    lst = []
    for i in range(size):
        lst.append(randint(min_number, max_number))
    return lst


def list_mix(lst: list) -> list:
    from random import randint
    for index in range(len(lst)):
        i_change = randint(0,len(lst)-1)
        lst[index], lst[i_change] = lst[i_change], lst[index]
    return lst



size_list = int(input('Enter amount of items in list: '))
min_value = int(input('Enter the minimum value in list: '))
max_value = int(input('Enter the maximum value in list: '))
list_original = fill_list(size_list, min_value, max_value)
print(f'Your list: {list_original}')
print(f'Your mixed list: {list_mix(list_original)}')