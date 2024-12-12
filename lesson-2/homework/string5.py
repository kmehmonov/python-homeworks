userInput = input("Biror matn kiriting. Men unlilar va undoshlar sonini sanayman: ")
vowels = "aAeEiIoOuU"
numberOfVowels = sum(1 for char in userInput if char in vowels)
allAlphaNumerics = sum(1 for char in userInput if char.isalpha())
print(f"unlilar {numberOfVowels} ta, undoshlar {allAlphaNumerics-numberOfVowels} ta.")
