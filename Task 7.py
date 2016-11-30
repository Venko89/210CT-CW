import math

def is_prime(n):
    #number 2 is a prime
    if n == 2:
        return True
    #if number divided by 2 brings a zero , or is smaller than 1 then its false
    if n%2 == 0 or n <= 1:
        return False
    #checking if the number multplied by itself +1 gets a prime number or turns false
    squared = int(math.sqrt(n)) + 1
    for divider in range(3, squared, 2):
        if n % divider == 0:
            return False
    return True
print(is_prime(133))
