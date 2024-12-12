def take_positive_number(prompt):
    while True:
        try:
            user_input = float(input(prompt))
            if user_input >= 0:
                return user_input
            else:
                print("Xatolik! Musbat son kiriting.")
        except ValueError:
            print("Xatolik! Haqiqiy turdagi musbat son kiriting.")


kilometers = take_positive_number("Konvertatsiya qilinishi kerak bo'lgan miqdorni kiriting:\n")
meters = int(kilometers * 1000)
centimeters = round((kilometers * 1000 - meters) * 100)

print(f"{kilometers}km = {meters}m va {centimeters}cm")
