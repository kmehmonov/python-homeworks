userInput = input("Matn kiriting: ")
vowels  = "aAeEoOuUiI"
symbol = "*"
for char in vowels:
    userInput = userInput.replace(char, symbol)
print(userInput)