

def invest(amount:float, rate:float, years:int) -> None:
    """
    tracks the growing amount of an investment over time
    """

    for i in range(1, years+1):
        amount = (1+rate/100) * amount
        print(f"year: {i}: {round(amount, 2)}")
    


initial_amount = float(input("Deposit uchun summa, so'm: "))
rate = float(input("Foiz, %: "))
years = int(input("Vaqt, yil: "))

invest(initial_amount, rate, years)