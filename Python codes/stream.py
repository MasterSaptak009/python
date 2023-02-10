def stream_cipher(key, plaintext):
    key_stream = [ord(k) for k in key]
    ciphertext = ''
    for i, char in enumerate(plaintext):
        ciphertext += chr(ord(char) ^ key_stream[i % len(key)])
    return ciphertext
print (stream_cipher('100110', 'saptak'))


def stream_cipher_decrypt(key, ciphertext):
    key_stream = [ord(k) for k in key]
    plaintext = ''
    for i, char in enumerate(ciphertext):
        plaintext += chr(ord(char) ^ key_stream[i % len(key)])
    return plaintext
print (stream_cipher_decrypt('100110', 'BQ@EP['))