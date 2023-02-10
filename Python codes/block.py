from Crypto.Cipher import AES

# 128-bit key (16 bytes)
key = b'Sixteen byte key'

# 128-bit initialiation vector (16 bytes)
iv = b'Sixteen byte iv'

# create a new AES cipher object using CBC mode
cipher = AES.new(key, AES.MODE_CBC, iv)

# plaintext to be encrypted
plaintext = b'The quick brown fox jumps over the lazy dog'

# padding the plaintext to a multiple of 16 bytes
padding = 16 - (len(plaintext) % 16)
plaintext = plaintext + bytes([padding] * padding)

# encrypt the plaintext
ciphertext = cipher.encrypt(plaintext)

# decryption
decipher = AES.new(key, AES.MODE_CBC, iv)
decrypted_plaintext = decipher.decrypt(ciphertext)

# removing the padding
decrypted_plaintext = decrypted_plaintext[:-decrypted_plaintext[-1]]

# display the results
print('Ciphertext:', ciphertext)
print('Decrypted plaintext:', decrypted_plaintext)
