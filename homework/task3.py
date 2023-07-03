chars = input('Please enter a four-character string for the variable chars: ')
word = input('Please enter a word to insert into the middle of chars: ')
if len(chars) !=4:
    print("Error: The length of chars should be exactly 4.")
else:
    middle_index = len(chars) // 2
    result = chars[:middle_index] + word + chars[middle_index:]
print("Result:", result)

