from rsa_keys import RSAKeyGenerator
from rsa_encrypt import RSAEncryptor
from rsa_decrypt import RSADecryptor
import json

def main():
    keygen = RSAKeyGenerator()

    while True:
        print("\n==== RSA Encryption Tool ====")
        print("1. Encrypt Text")
        print("2. Decrypt Text")
        print("3. Exit")
        option = input("Choose Option: ").strip()

        if option == "1":
            plaintext = input("Plaintext: ")
            public_key = keygen.get_public_key()  # (e, n)
            private_key = keygen.get_private_key()  # (d, n)

            print(f"\nPublic key (for encrypting): {json.dumps(public_key)}")
            print(f"Private key (for decrypting): {json.dumps(private_key)}")

            encryptor = RSAEncryptor(*public_key)
            encrypted = encryptor.encrypt_text(plaintext)
            print("\nEncrypted ciphertext :")
            print(json.dumps(encrypted))

        elif option == "2":
            ciphertext_str = input("Paste the ciphertext (e.g., [123, 456, ...]): ").strip()
            private_key_str = input("Paste the private key (e.g., [d, n]): ").strip()

            try:
                if not ciphertext_str or not private_key_str:
                    raise ValueError("Empty input provided.")

                ciphertext = json.loads(ciphertext_str)
                private_key = json.loads(private_key_str)

                if not isinstance(ciphertext, list) or not all(isinstance(i, int) for i in ciphertext):
                    raise ValueError("Ciphertext must be a list of integers.")
                if not isinstance(private_key, list) or len(private_key) != 2:
                    raise ValueError("Private key must be a list of two integers [d, n].")

                decryptor = RSADecryptor(*private_key)
                decrypted = decryptor.decrypt_text(ciphertext)
                print("\nDecrypted message:")
                print(decrypted)

            except Exception as e:
                print("Error:", e)

        elif option == "3":
            print("Exiting. Thank you!")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
