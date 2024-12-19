def is_prime(number : int) -> bool:
    """
    Check if a number is prime
    """
    if number < 2:
        return False
    
    until = int(number**0.5)+1
    for i in range(2, until):
        if number % i == 0:
            return False
    return True
    

print(is_prime(55))
