import re
password = input('Please enter your password: ')
x = True
while x:
    if (len(password) <= 8):
        break
    elif not re.search("[A-Z]", password):
        break 
    elif not re.search("[a-z]", password):
        break 
    elif not re.search("[0-9]", password):
        break 
    elif not re.search("\s", password):
        print('The password must contain at least one special character')
    else:
        print("Password Accepted")
        x = False
        break
if x:
    print("Not a Valid Password. Please try again!")