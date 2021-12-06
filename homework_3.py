# Не учитывать приоритеты

operations = []

current_element = ''

while current_element != '=':
    current_element = input()
    if current_element == '=':
        break
operations = operations + [current_element]
current_operator = ''
result = 0
for element in operations:
    if element.isdigit():
        element = int(element)

        if current_operator == '+' or current_operator == '':
            result = result + element
        elif current_operator == '-':
            result = result - element
        elif current_operator == '*':
            result = result * element
        else:
            result = result / element

    else:
        current_operator = element

print(result)
