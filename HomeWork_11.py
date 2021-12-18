input_measure = [(5, 'sm'), (3, 'in'), (1, 'ft'), (2, 'sa')]

'''
1m = 3.28084 ft
1m = 100 sm
1m = 39.3701 in
1m = 0.46869 sa
'''

def converter(length, measure):
    result = 0
    if measure == 'sm':
        result = length * 100
    elif measure == 'in':
        result = length * 39.3701
    elif measure == 'ft':
        result = length * 3.28084
    elif measure == 'sa':
        result = length * 0.46869
    else:
        result = 'Unknown'
    return result

for item in input_measure:
    if item[0] >= 1:
        converted = converter(item[0], item[1])
        print(converted)