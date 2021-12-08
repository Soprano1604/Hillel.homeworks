list1 = 'aaa bbb ccc aaa aaa ddd rrr'
count = 0
print('Перед вами список:\n' + list1)
while True:
    action = input(
        '''Введите слово, которое хотите заменить, "refresh", чтобы начать сначала или "exit" для завершения:\n''')

    if action == 'exit':
        print('Вы завершили программу замены слов.')
        break

    if action == "refresh":
        list1 = 'aaa bbb ccc aaa aaa ddd rrr'
        print('Вы начали сначала. Перед вами список:\n' + list1)
        continue

    if action not in list1:
        print("Выберите слово из списка:\n" + str(list1))
        continue

    if action in list1:

        action2 = input('Введите слово на которое вы хотите заменить:\n')

        if list1.find(action) != -1:
            list1 = list1.replace(action, action2, 1)

            count = list1.count(action)
            count += 1

            list1 = list1.replace(action, action2)

    print(list1)
    print('Произведено замен: ', count)
