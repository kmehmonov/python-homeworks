# 1-usul

userInput = input("Matn kiriting: ")
vowels  = "aAeEoOuUiI"
symbol = "*"
for char in vowels:
    userInput = userInput.replace(char, symbol)
print(userInput)

# 2-usul

userInput = input("Matn kiriting: ")
vowels  = "aAeEoOuUiI"
symbol = "*"
table = str.maketrans(vowels,symbol*len(vowels))
print(userInput.translate(table))