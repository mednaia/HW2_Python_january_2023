# Задайте список из n чисел последовательности (1 + 1/n)^n, выведеите его на экран, а так же сумму элементов списка.
# Пример:
# Для n=4 -> [2, 2.25, 2.37, 2.44]
# Сумма 9.06


def create_sequence(num: int):
    list = []
    for num in range(1, num+1):
        digit = round(((1+1/num)**num),2)
        list.append(digit)
    return list

def find_sum(series: list):
    result = 0
    for i in range(len(series)):
        result += series[i]
    return result


number = int(input('Input a number: '))
sequence = create_sequence(number)
print(f'Resulting sequence: {sequence}')
summ = find_sum(sequence)
print(f'Sum of sequences elements = {summ}')