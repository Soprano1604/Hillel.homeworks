# Переписать калькулятор чтоб можно было последовательно вводить неограниченное колличество чисел и операторов.
# Приоритеты операторов не учитывать
# Дополнительно и необязательно - учитывать приоритеты

while True:
    print('Please enter the number:')
    y = input()
    if y == 'exit':
        break
    for num in range(2, int(y)):
        if all(num % x != 0 for x in range(2, num)):
            print(num)
