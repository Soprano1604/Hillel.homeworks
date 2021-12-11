# Написать регулярное выражение для проверки номера телефона
import re

while True:
    number = input('Введите номер для проверки: \n')
    if number == 'exit':
        break
    print(bool(re.match(r'(\s*)?(\+)?([- _():=+]?\d[- _():=+]?){10,14}(\s*)?', number)))
