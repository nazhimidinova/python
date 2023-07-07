lst = [i for i in range(1, 51)]
print(lst)


even_num = [ i for i in lst if i % 2 == 0 ]
print(even_num)
sum_even_numbers = 0.0
for even_num in even_num:
    sum_even_numbers += even_num


odd_num = [ i for i in lst if i % 2 !=0 ]
print(odd_num)
product_odd_numbers = 1
for odd_num in odd_num:
    product_odd_numbers *= odd_num



largest_number = max(lst)

print('Sum of all even numbers in the list is: ', sum_even_numbers)
print('Product of all odd numbers in the list is: ', product_odd_numbers)
print('Largest_number: ', largest_number)

