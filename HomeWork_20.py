import json

file_object = open('DPPBVV1U.json', 'r')
my_object = (file_object.read())
my_result = json.loads(my_object)

sum_runtime = 0
for obj in my_result['_embedded']['episodes']:
        sum_runtime += my_result['runtime']
print(f'Total length of episodes:', sum_runtime, 'mins')


for obj in my_result['_embedded']['episodes']:
        season = obj['season']
        series = obj['number']
        named = obj['name']
        link = obj['url']
        description = obj['summary']
        print(f'Season', season, 'Episode', series)
        print(f'Name -', named)
        print(f'Description of episode:', description)
        print(f'More about:', link)

file_object.close()