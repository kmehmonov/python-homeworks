userInput = input("Matn kiriting. Qisqartma qaytaraman: ")
qisqartma=''
for word in userInput.split():
    qisqartma+=word[0].upper()
print("Qisqartma:", qisqartma)