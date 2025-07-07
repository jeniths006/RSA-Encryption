import random
from math import gcd
from sympy import isprime

class RSAKeyGenerator:
    def __init__(self, bit_length=6):
        self.p = self.generate_prime(bit_length)
        self.q = self.generate_prime(bit_length)
        self.n = self.p * self.q
        self.phi_n = (self.p - 1) * (self.q - 1)
        self.e = self.generate_public_key()
        self.d = pow(self.e, -1, self.phi_n)

    def generate_prime(self, bit_length):
        while True:
            num = random.randint(10**(bit_length-1), 10**bit_length - 1)
            if isprime(num):
                return num

    def generate_public_key(self):
        for i in range(3, self.phi_n):
            if gcd(i, self.phi_n) == 1:
                return i
        raise Exception("No valid public key found")

    def get_public_key(self):
        return (self.e, self.n)

    def get_private_key(self):
        return (self.d, self.n)
