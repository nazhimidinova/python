my_set = set([1, 2, 3, 4, 5])
print(my_set)

set = {23,45,67}
set.add(22)
print(set)
set.remove(67)
print(set)

set = {67, 12, 46}
for element in set:
    print(element)


set1 = {12, 13, 14, 15}
set2 = {15, 22, 23, 24, 25}

# Union of sets
union = set1 | set2
print(union)

# Intersection of sets
intersection = set1 & set2
print(intersection)

my_set = {x ** 3 for x in range(3)}
print(my_set)

candidate1 = {'name': 'John', 'age': 25, 'city': 'New York'}
candidate2 = {'name': 'Josh', 'age': 29, 'city': 'Chicago'}
print(candidate1['name'])
print(candidate2['age'])
candidate1['height'] = '6.2'
candidate2['height'] = '5.9'
print(candidate1)
print(candidate2)
candidate1['height'] = '6'
print(candidate1)
del candidate2['height']
print(candidate2)

for key in candidate1:
    print(key)

for value in candidate2.values():
    print(value)

for key, value in candidate1.items():
    print(key, value)

if 'height' in candidate1:
    print('They key "height" exists in the candidate set.')
else:
    print('They key "height" is not in the set.')

veg = ["potato", "tomato", "eggplant", "carrot"]
my_dict = {num+1: veg for num, veg in enumerate(veg)}
print(my_dict)