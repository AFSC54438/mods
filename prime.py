from math import sqrt

def check_prime(n):
    if (n <= 1) or (n != int(n)):
        return False
    
    if n == 2:
        return True
    
    if n % 2 == 0 and n > 2:
        return False

    k = int(sqrt(n))

    for i in range(3, k + 1, 2):
        if n % i == 0:
            return False
        
    return True
