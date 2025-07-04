# 🔐 RSA Encryption Tool in Python

This is a simple implementation of RSA public-key cryptography. The script generates random prime numbers, calculates public/private keys, and encrypts or decrypts user-provided input using modular exponentiation.

## 📌 Features

- Prime number generation
- Key pair (public/private) generation
- Modular exponentiation for encryption/decryption
- Works on plaintext integers

## 🚀 How to Run

```bash
python rsa.py


# Example Output

Generated primes: p = 149, q = 107
n = 15943
phi(n) = 15788
Public key (e): 5
Private key (d): 9473

Enter number to encrypt: 13
Encrypted: 3713
Decrypted: 13


💡 Future Improvements
Encrypt full text strings

Add file-based key saving/loading

Build a GUI or CLI with argparse

Use large primes for real security

🧠 Concepts Covered
Modular arithmetic

Greatest common divisor (GCD)

Modular inverse

Public-key cryptography basics



