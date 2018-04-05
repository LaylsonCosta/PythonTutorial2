"""
Nested Dictionary
d = {'k1': {'nestk1':'nestvalue1', 'nestk2':'nestvalue2'}}
d['k1']['nestk1']
"""

cars = {'bmw': {'model': '550i', 'year': '2016'},
        'benz': {'model': 'E350', 'year': '2017'}}
print(cars)

print(cars['bmw'])
print(cars['benz'])

print("*************************")
bmw_year = cars['bmw']['year']
print(bmw_year)
print(cars['benz']['model'])

"""teste
print("********************")
d{'key1': {1, 2, 3}, "key2": {4, 5, 6}}
print(cars['key1'][2])
"""