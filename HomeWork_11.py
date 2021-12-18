input_measure = [(5, 'sm'), (3, 'in'), (1, 'ft'), (2, 'sa'), (0.5, 'sm')]

'''
1m = 3.28084 ft
1m = 100 sm
1m = 39.3701 in
1m = 0.46869 sa
'''

def converter(measure_object):
    convert_type = measure_object[1]
    length = measure_object[0]
    result = 0
    if convert_type == 'sm':
        result = length * 100
    elif convert_type == 'in':
        result = length * 39.3701
    elif convert_type == 'ft':
        result = length * 3.28084
    elif convert_type == 'sa':
        result = length * 0.46869
    else:
        result = 'Unknown'
    return result

result = map(converter, filter(lambda itm_in: True if itm_in[0] >= 1 else False, input_measure))
for itm in result:
    print(itm)