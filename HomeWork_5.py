# Написать программу которая выводит простые числа до введённого пользователем.

while True:
    print('Please enter the number:')
    y = input()
    if y == 'exit':
        break
    for num in range(2, int(y)):
        if all(num % x != 0 for x in range(2, num)):
            print(num)
