# 1-usul

prime_numbers = []
final = 100
i = 2
while i <= final:
    until = int(i**0.5)
    j = 2
    is_prime = True
    
    while j <= until:
        if i % j == 0:
            is_prime = False
            break 
        j += 1

    if is_prime:
        prime_numbers.append(i)
    i += 1

print("method-1:", prime_numbers)

# 2-usul

prime_numbers = []
final = 100
for number in range(2, final):
    until = int(number**0.5)+1
    for dev in range(2, until):
        if number % dev == 0:
            break
    else:
        prime_numbers.append(number)
print("method-2:", prime_numbers)

