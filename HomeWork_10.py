# Написать функцию которая переводит метры в сантиметры, футы, дюймы, сажни

metr = float(input('Введите значение в метрах: '))
def converter(metr, convert_type):
    if convert_type == 'sm':
        result = f'{(metr * 100)} сантиметров'
    elif convert_type == 'ft':
        result = f'{(metr * 3.281)} футов'
    elif convert_type == 'in':
        result = f'{(metr * 39.37)} дюймов'
    elif convert_type == 'sj':
        result = f'{(metr / 1.829)} саженей'
    return result

print(converter(metr, 'sm'))
print(converter(metr, 'ft'))
print(converter(metr, 'in'))
print(converter(metr, 'sj'))