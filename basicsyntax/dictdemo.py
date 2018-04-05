"""
Data type store more than one value in one variable name, in terms of key value pairs
Dictionary items are in brackets {} in key:value pairs, separated with "," {'k1':'v1', 'k2':'v2'}
Not sequenced, no indexing -> Mapping 
"""

car = {'make': 'bmw', 'model': '550i', 'year': 2016}

d = {}

print(car)

model = car['model']

print(car['year'])
print(model)
print(d)


# add more items
print('**************')
d['one'] = 1
d['two'] = 2
print(d)

# operations
print('**************')
sum_1 = d['two'] + 8
print(sum_1)

# changing values
print('*********************')
d['two'] = d['two'] + 8
print(d)
