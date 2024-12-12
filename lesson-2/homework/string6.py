firstString = input("Birinchi stringni kiriting: ")
secondString = input("Ikkinchi stringni kiriting: ")

if firstString in secondString:
    print(f"{firstString=} {secondString=} ichida bor")
elif secondString in firstString:
    print(f"{secondString=} {firstString=} ichida bor")
else:
    print("Bu stringlar bir birini qamrab olmaydi")
