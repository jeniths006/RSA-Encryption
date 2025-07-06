from rsa_keys import RSAKeyGenerator
from rsa_encrypt import RSAEncryptor
from rsa_decrypt import RSADecryptor

def main():
    keygen = RSAKeyGenerator()

    print("Choose option:")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Exit")
    option = input("Choose Option: ")
    if option == "1":
        plaintext = input("Plaintext: ")
        public_key = keygen.get_public_key()
        private_key = keygen.get_private_key()
        print(f"Public key: ({public_key})")
        print(f"Private key: ({private_key})")

        encryptor = RSAEncryptor(*public_key)
        encrypted = encryptor.encrypt_text(plaintext)
        print("Encrypted:", encrypted)








if __name__ == "__main__":
    main()
