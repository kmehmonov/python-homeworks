status = True
while status:
    user_input = input("Haqiqiy son kiriting: ")
    try:
        print(round(float(user_input), 2))
        status = False
    except:
        print("Xatolik!")




