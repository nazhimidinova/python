secret_number = 777
max_attempts = 3
attempts = 0

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

while attempts < max_attempts:
    number = int(input("Please enter a number: "))

    if number == secret_number:
        print("Well done, muggle! You are free now.")
        break
    else:
        attempts += 1
        print("Ha ha! You're stuck in my loop!")

if attempts == max_attempts:
    print("Oops, you've tried three times and couldn't guess the secret number.")
    print("Hint: The secret number is a three-digit number between 700 and 800.")

while attempts >= max_attempts:
    number = int(input("Please enter a number: "))

    if number == secret_number:
        print("Well done, muggle! You are free now.")
        break
    else:
        print("Ha ha! You're stuck in my loop!")

print("Game over!")


