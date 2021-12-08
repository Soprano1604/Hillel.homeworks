list1 = 'aaa bbb ccc ddd aaa'
print(list1)
action = input("Выберите слово:\n")
action2 = (input("Введите слово:\n"))
print("Замена выполнена:")
print(list1.replace(action, action2))
print("Количество замен:")
print(list1.count(action))

