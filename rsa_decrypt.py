class RSADecryptor:
    def __init__(self, d, n):
        self.d = d
        self.n = n

    def decrypt_number(self, ciphertext):
        return pow(ciphertext, self.d, self.n)

    def decrypt_text(self, ciphertext):
        return ''.join(chr(self.decrypt_number(num)) for num in ciphertext)
