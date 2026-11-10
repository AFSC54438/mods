from cs50 import get_string
from math import gcd
from random import randint
from sympy import isprime

def main():
    my_message = get_string("Message: ")

    print(len(my_message))
    m = encode_message(my_message)

    private_key, public_key = generate_rsa_key()
    
    if m >= public_key["n"]:
        raise ValueError("Message too long for this key")

    c = encrypt(m, public_key)

    print(f"Message encrypted. Ciphertext: {c}")

    print("Sending the message to your friend...")

    print("Decrypting message...")

    decrypted_m = decrypt(c, private_key)

    print(f"The message is: {decode_to_text(decrypted_m)}")
  

def generate_rsa_key():
    p = generate_random_prime()
    q = generate_random_prime()

    n = p*q

    phi_n = (p-1) * (q-1)

    encrypt_exp = get_e(2, phi_n)
    decrypt_exp = get_d(encrypt_exp, phi_n)

    public_key = {"n" : n, "e" : encrypt_exp}
    private_key = {"n" : n, "d" : decrypt_exp}

    return private_key, public_key

def encrypt(m, public_key):
    e = public_key["e"]
    n = public_key["n"]

    return pow(m, e, n)

def decrypt(ciphertext, private_key):
    d = private_key["d"]
    n = private_key["n"]

    return pow(ciphertext, d, n)
    
    
def encode_message(text):
    return int.from_bytes(text.encode(), "big")

def decode_to_text(m):
    return m.to_bytes((m.bit_length() + 7) // 8, "big").decode()


def generate_random_prime():
    n = randint(2, 999999999999999999999999999999999999999999999999999999)

    while isprime(n) == False:
        n = randint(2, 999999999999999999999999999999999999999999999999999999)

    return n


def check_coprime(a, b):
    return gcd(a, b) == 1


def get_e(n, phi_n):
    e = randint(n, phi_n)

    while check_coprime(e, phi_n) == False:
        e = randint(n, phi_n)

    return e


def get_d(n, modulo):
    old_r, r = n, modulo
    old_s, s = 1, 0

    while r != 0:
        quotient = old_r // r

        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s

    if old_r != 1:
        return None

    return old_s % modulo


if __name__ == "__main__":
    main()

    
