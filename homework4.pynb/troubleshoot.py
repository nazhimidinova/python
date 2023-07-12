def check_even(lst):
    list_even = []
    for i in lst:
        if i % 2 == 0:
            list_even.append(i)

    return list_even


try:
    check_even(['string', 2])
except Exception as e:
    print('you code have an error', e)
    inp = input('You provided a wrong input, please give the list of strings: ')
    new_inp = list(inp)
    check_even(new_inp)

    print(check_even(new_inp))