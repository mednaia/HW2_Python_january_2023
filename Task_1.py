# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

#  Variant 1

# def sum_of_digit(figure):
#     sum = 0
#     for i in str(figure):
#         if i != ".":
#             sum += int(i)
#     return sum


# number = float(input('Input a real number: '))

# print(f'Sum of digits {number} is {sum_of_digit(number)}')

# Variant 2

number = str(input('Input a real number: '))

number = number.replace('.', '')
print(sum(map(int,str(number))))