
# Masala shartida faqat butun son nazarda tutilgan bo'lsa.
def take_number(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print(f"Xatolik! butun turdagi son kiriting.")

print("Kiritilgan sonning oxirgi raqamini qaytaraman.")
number = take_number("Butun son kiriting: ")
print(f"sonning oxirgi raqami: {str(number)[-1]}")




