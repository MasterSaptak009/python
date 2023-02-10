def rail_fence_encrypt(plaintext, rails):
    rail = [[None] * len(plaintext) for i in range(rails)]
    rail_number, direction = 0, "down"
    for i in range(len(plaintext)):
        rail[rail_number][i] = plaintext[i]
        if rail_number == 0:
            direction = "down"
        if rail_number == rails - 1:
            direction = "up"
        rail_number += 1 if direction == "down" else -1
    result = []
    for r in rail:
        for char in r:
            if char is not None:
                result.append(char)
    return "".join(result)

def rail_fence_decrypt(ciphertext, rails):
    rail = [[None] * len(ciphertext) for i in range(rails)]
    rail_index = list(range(len(ciphertext)))
    rail_number, direction = 0, "down"
    for i in range(len(ciphertext)):
        rail[rail_number][i] = rail_index[i]
        if rail_number == 0:
            direction = "down"
        if rail_number == rails - 1:
            direction = "up"
        rail_number += 1 if direction == "down" else -1
    result = [None] * len(ciphertext)
    index = 0
    for i in range(rails):
        for j in range(len(ciphertext)):
            if rail[i][j] is not None:
                result[rail[i][j]] = ciphertext[index]
                index += 1
    return "".join(result)

print(rail_fence_encrypt("saptak",3))
print(rail_fence_decrypt("saatkp",3))