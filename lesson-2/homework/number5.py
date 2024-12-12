def take_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print(f"Xatolik! haqiqiy turidagi son kiriting.")

celsius = take_number("Selsiydagi qiymatni kiriting: ")
print(f"{celsius} Celsius = {celsius*9/5+32} Fahrenheit")