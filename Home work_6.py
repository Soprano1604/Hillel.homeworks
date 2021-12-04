# Улучшить определитель марок из предыдущего урока, так, чтоб можно было бесконечно вводить модель
# и получать марку пока пользователь не напишет слово exit

ford = ['mondeo', 'focus', 'kuga']
fiat = ['tipo', 'panda', '500']
renault = ['clio', 'megan', 'duster']

print('Please, enter the name of the car:')

while True:
    action = input()
    if action == 'exit':
        break
    if action in ford:
        print('ford\nPlease, re-enter or write "exit" to finish:')
    elif action in fiat:
        print('fiat\nPlease, re-enter or write "exit" to finish:')
    elif action in renault:
        print('renault\nPlease, re-enter or write "exit" to finish:')
    else:
        print("Please, enter the correct name")
