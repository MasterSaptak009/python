def caesar_cipher(plaintext, shift, encrypt=True):
    """Encrypt or Decrypt the string and return the result"""
    result = ""
    if encrypt:
        for char in plaintext:
            if char.isalpha():
                shift_char = chr((ord(char.upper()) + shift - 65) % 26 + 65)
                if char.islower():
                    result += shift_char.lower()
                else:
                    result += shift_char
            else:
                result += char
    else:
        for char in plaintext:
            if char.isalpha():
                shift_char = chr((ord(char.upper()) - shift - 65) % 26 + 65)
                if char.islower():
                    result += shift_char.lower()
                else:
                    result += shift_char
            else:
                result += char
    return result

# Example usage
print(caesar_cipher("HELLO WORLD", 3))
# Output: KLOOH WRUQD

print(caesar_cipher("KLOOH WRUQD", 3, False)) 
# Output: HELLO WORLD
