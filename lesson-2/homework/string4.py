userInput = input("Biror matn/so'z kiriting. Men palindromlikka tekshiraman: ")
if userInput==userInput[::-1]:
    print("Siz kiritgan matn/so'z palindrom")
else:
    print("Siz kiritgan matn/so'z palindrom emas")