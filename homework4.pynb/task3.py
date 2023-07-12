def average(*args):
    if not args:
        print('ZeroDivisionError. Please try again: ')
        return None
    total = sum(args)
    average = total / len(args)
    return average
    

print(average(1,2,3,4,5,6,7,8,9,10))