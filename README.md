# RSA Encryption Tool in Python

This project is a simple and extendable implementation of RSA public-key cryptography in Python. It demonstrates the generation of RSA key pairs, encryption of plaintext messages, and decryption of ciphertext using modular arithmetic and number theory.

## Features

- Random prime number generation using probabilistic testing
- RSA key pair generation (public and private)
- Full-text encryption (character-by-character)
- Modular exponentiation for secure encryption and decryption
- JSON-formatted output for easy key and ciphertext reuse
- Interactive command-line interface with menu navigation

## How to Run

1. Clone the repository:
   git clone https://github.com/yourusername/rsa-encryption-tool.git
   cd rsa-encryption-tool

2. Install dependencies:
   pip install sympy

3. Run the program:
   python main.py

Note: Requires Python 3.6 or higher.

## Example Usage

==== RSA Encryption Tool ====
1. Encrypt Text
2. Decrypt Text
3. Exit
Choose Option: 1

Plaintext: hello

Public key (for encrypting): [257, 3233]
Private key (for decrypting): [937, 3233]

Encrypted ciphertext (copy this):
[1800, 1311, 2202, 2202, 2385]

Then later:

Choose Option: 2
Paste the ciphertext: [1800, 1311, 2202, 2202, 2385]
Paste the private key: [937, 3233]

Decrypted message:
hello

## Project Structure

rsa-encryption-tool/
├── main.py              # Main program with interactive menu
├── rsa_keys.py          # RSA key generation logic
├── rsa_encrypt.py       # Encryption module
├── rsa_decrypt.py       # Decryption module
├── README.md            # Project documentation

## Concepts Demonstrated

- Prime number generation
- Modular exponentiation
- Euler's totient function
- Greatest common divisor (GCD)
- Modular inverse calculation
- Public-key cryptography fundamentals

## Future Improvements

- Save and load keys/ciphertext from files
- Add unit tests and CI integration
- Support for large prime sizes for realistic security
- GUI interface using Tkinter or CLI enhancement using argparse
- Web version using Flask or FastAPI

## License

This project is licensed under the MIT License.
