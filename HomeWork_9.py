# Написать приложение которое будет находить первый повторяющийся элемент среди введённых пользователем
import re

while True:
    numbers = input('Введите числовую строку для проверки: \n')

    if numbers == 'exit':
        break

    result = re.search(r'(\d+)(?=\d\1)', numbers)
    print(result.group())
