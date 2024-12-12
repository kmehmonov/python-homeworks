import math

def take_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print(f"Xatolik! Haqiqiqy turdagi son kiriting.")

def is_approximately_e(number, tolerance):
    return abs(number - math.e) <= tolerance

print("e ning sizdagi qiymatini delta aniqlik bilan haqiqiy qiymatiga mosligini tekshiruvchi dastur")

number = take_number("e ning sizdagi qiymatini kiriting.\n")
tolerance = take_number("aniqlik darajasini kiriting, masalan 0.01\n")

if is_approximately_e(number, tolerance):
    print(f"{number} son {tolerance} aniqlik bilan {math.e} ga mos.")