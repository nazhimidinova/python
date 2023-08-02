user_word = input("Please enter a word: ")
user_word = user_word.upper()
word_without_vowels = ""
for letter in user_word:
    if letter == "A" or letter == "E" or letter == "I" or letter == "O" or letter == "U":
        continue
    else:
        word_without_vowels +=letter

print(word_without_vowels)
