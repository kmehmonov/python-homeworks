def take_number(prompt, number_type):
    while True:
        try:
            return number_type(input(prompt))
        except ValueError:
            print(f"Xatolik! {number_type.__name__} turidagi son kiriting.")

print("n ta son kiriting, eng kattasini aniqlab beraman.")
print("Nechta son kiritmoqchisiz?")
n = take_number("Butun son kiriting: ", int)

max_number = float('-inf')
for i in range(1, n + 1):
    number = take_number(f"{i}-sonni kiriting: ", float)
    max_number = max(max_number, number)

print(f"Eng katta son: {max_number}")
