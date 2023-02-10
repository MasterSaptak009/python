def encrypt(plaintext, key):
    a, b = key
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            shift = (ord(char.upper()) - 65) * a + b
            cipher_char = chr((shift % 26) + 65)
            if char.islower():
                ciphertext += cipher_char.lower()
            else:
                ciphertext += cipher_char
        else:
            ciphertext += char
    return ciphertext

def decrypt(ciphertext, key):
    a, b = key
    plaintext = ""
    a_inv = 0
    for i in range(26):
        if (a * i) % 26 == 1:
            a_inv = i
            break
    for char in ciphertext:
        if char.isalpha():
            shift = (ord(char.upper()) - 65 - b + 26) * a_inv
            plain_char = chr((shift % 26) + 65)
            if char.islower():
                plaintext += plain_char.lower()
            else:
                plaintext += plain_char
        else:
            plaintext += char
    return plaintext

key = (5, 8)
plaintext = "Affine cipher example"
ciphertext = encrypt(plaintext, key)
print("Ciphertext:", ciphertext)
decrypted_text = decrypt(ciphertext, key)
print("Decrypted text:", decrypted_text)