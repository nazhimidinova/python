import re
def check_password(password):
    if len(password) < 8:
        return "The password must be at least 8 characters long."
    if not re.search("[A-Z]", password):
        return "The password should contain at least one uppercase letter."
    if not re.search("[a-z]", password):
        return "The password should contain at least one lowercase letter."
    if not re.search("[0-9]", password):
        return "The password should contain at least one digit."
    if not re.search("[@#$%^&+=]", password):
        return "The password should contain at least one special character."
    return "Password Accepted!"
while True:
    password = input('Enter a password: ')
    result = check_password(password)
    if result == "Password accepted.":
        print(result)
        break
    else:
        print('Invalid password:', result)
        print('Please try again.')