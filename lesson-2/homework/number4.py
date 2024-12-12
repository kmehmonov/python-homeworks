def take_positive_number(prompt):
    while True:
        try:
            user_input = float(input(prompt))
            if user_input >= 0:
                return user_input
            else:
                print("Xatolik! Musbat son kiriting.")
        except ValueError:
            print("Xatolik! Musbat son kiriting.")

bolinuchi = take_positive_number("Bo'linuvchini kiriting: ")
boluvchi = take_positive_number("Bo'luvchini kiriting: ")

bolinma, qoldiq = divmod(bolinuchi, boluvchi)

print(f"bo'linma={int(bolinma)}; qoldiq={int(qoldiq)}.")