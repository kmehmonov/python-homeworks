

def convert_to_cel(fahrenheit: float) -> float:
    """ Converting °F to °C """
    return round((fahrenheit - 32) * 5/9, 2)

def convert_to_far(celsius: float) -> float:
    """ Converting °C to °F """
    return round(celsius * 9/5 + 32, 2)


far = float(input("Enter a temperature in °F: "))
print(f"{far} °F = {convert_to_cel(far)} °C")

cel = float(input("Enter a temperature in °C: "))
print(f"{cel} °C = {convert_to_far(far)} °F")





