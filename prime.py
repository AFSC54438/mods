from math import sqrt

def check_prime(n):
    if (n <= 1) or (n != int(n)):
        return False
    
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
        
    return True
