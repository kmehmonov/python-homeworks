
def nfactor(n : int) -> int:
    """
    Prints all natural divisors of a given number n.
    """

    until = n // 2 + 1
    print(n, "ning natural bo'luvchilari:", sep="")

    for i in range(1, until):
        if n % i == 0:
            print(i)

    print(n)



number = int(input("Son kiriting, natural bo'luvchilarini aniqlaymiz: "))
nfactor(number)

