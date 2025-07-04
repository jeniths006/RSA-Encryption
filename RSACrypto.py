import random
from math import gcd


def is_prime(n):
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
        if is_prime(num):
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
cipher_text_number = encrypter(plaintext, e, n)
print("Encrypted Number: ", cipher_text_number)


def decryptor(cipher_text, d, n):
    return (cipher_text ** d) % n


deciphered_text = decryptor(cipher_text_number, d, n)
print("Deciphered text: ", deciphered_text)



def encrypt_text(message, e, n):
    encrypted_chars = []
    for char in message:
        encrypted_chars.append(encrypter(ord(char), e, n))
    return encrypted_chars

encrypted_message = encrypt_text("Hi", e, n)
print("Encrypted text: ", encrypted_message)

def decrypt_text(cipher_message, d, n):
    decrypted_chars = []
    for char in cipher_message:
        decrypted_chars.append(chr(decryptor(char, d, n)))
    return decrypted_chars

print(''.join(decrypt_text(encrypted_message, d, n)))





















