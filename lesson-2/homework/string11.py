userInput = input("Text bering, ichida raqam bor/yo'qligini ayataman.\n")
if any(True for char in userInput if char.isdigit()):
    print("Text ichida raqam mavjud")
else:
    print("Text ichida raqam mavjud emas")


