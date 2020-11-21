import hashlib
import subprocess
import pyAesCrypt
import sys

if len(sys.argv) <= 2:
    print("\nLet's encrypt or decrypt your file.\n")
    print("Usage : python3 crypt.py <encrypt/decrypt> <filename>")

else:
    choose = sys.argv[1]
    directory = sys.argv[2]
    password = input("Enter key: ")
    hash = hashlib.md5()
    hash.update(password.encode())
    buffer = 512 * 1024

    if choose == "encrypt" or choose == "e":
        pyAesCrypt.encryptFile(directory, directory + ".aes", hash.hexdigest(),
                               buffer)
        subprocess.call(["rm", directory])
        print("[Encrypted] " + directory + ".aes")
    elif choose == "decrypt" or choose == "d":
        pyAesCrypt.decryptFile(directory, directory[:-4], hash.hexdigest(),
                               buffer)
        subprocess.call(["rm", directory])
        print("[Decrypted] " + directory)
    else:
        print(
            "Bad input! Use words like 'encrypt' or 'decrypt' or characters like 'e' or 'd'"
        )

