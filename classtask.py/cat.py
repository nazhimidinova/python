def check_string(string):
    if len(string) > 100:
        print("Your string has more than 100 letters")
        return False

    words = string.split()
    if len(words) > 0:
        first_word = words[0]
        if len(first_word) < 5 and len(first_word) <= 2:
            print("Your string does not meet the requirement")
            return False

    return True

input_string = "The cat is black, and it likes to sleep on the mat. Its name is Max."

if check_string(input_string):
    print("Success")
