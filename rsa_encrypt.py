class RSAEncryptor:
    def __init__(self, e, n):
        self.n = n
        self.e = e

    def encrypt_number(self, plaintext):
        return pow(plaintext, self.e, self.n)

    def encrypt_text(self, message):
        return [self.encrypt_number(ord(char)) for char in message]
