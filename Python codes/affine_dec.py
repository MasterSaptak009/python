def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mod_inv(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def affine_cipher(text, key, mode):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    a, b = key
    result = ""
    
    if gcd(a, 26) != 1:
        return "Error: a and 26 are not relatively prime."
    
    a_inv = mod_inv(a, 26)
    
    if mode == "encrypt":
        for char in text:
            if char in alphabet:
                result += alphabet[(a * alphabet.index(char) + b) % 26]
            else:
                result += char
    elif mode == "decrypt":
        for char in text:
            if char in alphabet:
                result += alphabet[(a_inv * (alphabet.index(char) - b)) % 26]
            else:
                result += char
    return result


user_input = affine_cipher("hello",[7,2],"encrypt")
print(affine_cipher("hello",[7,2],"encrypt"))
print(affine_cipher(user_input,[7,2],"decrypt"))