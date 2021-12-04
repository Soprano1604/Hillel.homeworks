# Переписать калькулятор чтоб можно было последовательно вводить неограниченное колличество чисел и операторов.
# Приоритеты операторов не учитывать
# Дополнительно и необязательно - учитывать приоритеты

num1 = input()
action = input()
num2 = input()
while True:
    if (action in ['+', '-', '*', '/']) and num1.isdigit() and num2.isdigit():
        num1 = int(num1)
        num2 = int(num2)

        if action == '*':
            print(num1 * num2)
            continue

        elif action == '/':
            print(num1 / num2)
            continue

        elif action == '+':
            print(num1 + num2)
            continue

        elif action == '-':
            print(num1 - num2)
            continue


        else:
            print('Error')
    if print('exit'):
        break

# a = float(input('Введите первое число: '))
# operator = input('Введите операцию: ')
# b = float(input('Введите второе число: '))
#
# while True:
#     if operator == '+':
#         c = a + b
#         print(c)
#         continue
#     elif operator == '-':
#         c = a - b
#         print(c)
#         continue
#     elif operator == '*':
#         c = a * b
#         print(c)
#         continue
#     elif operator == '/':
#         c = a / b
#         print(c)
#         continue
#     else:
#         break