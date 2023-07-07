#homework
tup = (1,4,9,16,25,36,49,64,81,100)
sum = 0.0
for tup in tup:
    sum += tup
print('Total value of tup:', sum)


companies = ['Meta', 'Dior', 'Chanel', 'Google', 'Tesla']
for index in range(len(companies)):
    print("Current index: ", index, '| Current company: ', companies[index])


top_companies = ['Google', 'IBM', 'Meta', 'Dior', 'Tesla']
companies[0], companies[4] = companies[4], companies[0]
print(companies)
if 'Dior' in top_companies:
    print('Dior is in top_companies')

top_companies = ['Google', 'IBM', 'Meta', 'Dior', 'Tesla']
companies.sort()
print(companies)

num = [1, 5, 7, -2, -9, 0]
num.sort(reverse=True)
print(num)
if 5 in num:
    print('5 is in the num')

destination = ['Dubai', 'Maldives', 'Kyrgyzstan', 'Vietnam', 'Japan']
country = input('Which country do you want to visit?: ')
if country in destination:
    print('You can visit this country without visa')
else:
    print('You can not visit this country without visa')



name = ['Aika', 'Jennifer', 'Zoe']
name_new = name[:2]
name[0] = 'Aijamal'
print('Original:', name, 'New', name_new)



 
