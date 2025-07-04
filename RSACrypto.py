import random
from math import gcd


def isPrime(n):
    if n<= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i+2) == 0:
            return False
        i += 6
    return True


def generatePrime(start = 100, end = 300):
    while True:
        num = random.randint(start, end)
        if isPrime(num):
            return num

p = generatePrime()
q = generatePrime()

#print("P", p)
#print("Q", q)


n = p * q
phi_n = n - p - q + 1


def generate_public_key(phi_n):
    i = 3
    while i < phi_n:
        if gcd(i, phi_n) == 1:
            return i
            break
        i += 1

e = generate_public_key(phi_n)
print("Public Key:", e)


d = pow(e, -1, phi_n)
print("Private Key: ", d)


def encrypter(plaintext, e, n):
    return (plaintext ** e) % n



plaintext = int(input("Please enter number to encrypt: "))
cipher_text = encrypter(plaintext, e, n)
print("Encrypted Number: ", cipher_text)


def decryptor(cipher_text, d, n):
    return (cipher_text ** d) % n


deciphered_text = decryptor(cipher_text, d, n)
print("Deciphered text: ", deciphered_text)









