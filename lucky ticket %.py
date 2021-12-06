count = 0

for ticket_number in range(0, 1000000, 1):
    num6 = ticket_number % 10
    ostatok = ticket_number // 10
    num5 = ostatok % 10
    ostatok = ostatok // 10
    num4 = ostatok % 10
    ostatok = ostatok // 10
    num3 = ostatok % 10
    ostatok = ostatok // 10
    num2 = ostatok % 10
    ostatok = ostatok // 10
    num1 = ostatok % 10

    if num1+num2+num3 == num4+num5+num6:
        count += 1

print('Hare are: ' + str(count))