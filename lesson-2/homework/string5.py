 # 1 - usul

userInput = input("Biror matn kiriting. Men unlilar va undoshlar sonini sanayman: ")
vowels = "aAeEiIoOuU"
numberOfVowels = sum(1 for char in userInput if char in vowels)
allAlphaNumerics = sum(1 for char in userInput if char.isalpha())
print(f"unlilar {numberOfVowels} ta, undoshlar {allAlphaNumerics-numberOfVowels} ta.")

# 2 - usul

userInput = input("Biror matn kiriting. Men unlilar va undoshlar sonini sanayman: ")
vowels = "aAeEiIoOuU"
numberOfVowels = 0
numberOfConsonants = 0
for char in userInput:
    if char.isalpha():
        if char in vowels:
            numberOfVowels += 1
        else:
            numberOfConsonants += 1

print(f"unlilar {numberOfVowels} ta, undoshlar {numberOfConsonants} ta.")