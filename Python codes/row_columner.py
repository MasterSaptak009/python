def row_column_transposition(text, key): 
    row = len(key) 
    col = len(text)//row + (len(text) % row != 0) 
    plain_matrix = [["" for j in range(col)] for i in range(row)] 
    k = 0 
    for i in range(row): 
        for j in range(col): 
            if k < len(text): 
                plain_matrix[i][j] = text[k] if k < len(text) else "X"
                k += 1 
    encrypted = "" 
    for j in range(col): 
        for i in range(row): 
            encrypted += plain_matrix[i][j] if str(i+1) in key else "X"
    return encrypted 
 
def row_column_transposition_decrypt(cipher_text, key): 
    row = len(key) 
    col = len(cipher_text)//row + (len(cipher_text) % row != 0) 
    plain_matrix = [["" for i in range(row)] for j in range(col)] 
    k = 0 
    for j in range(col): 
        for i in range(row): 
            if k < len(cipher_text): 
                plain_matrix[j][i] = cipher_text[k] 
                k += 1 
    decrypted = "" 
    for i in range(row): 
        for j in range(col): 
            decrypted += plain_matrix[j][key.index(str(i+1))] if str(i+1) in key else "X" 
    return decrypted if decrypted[-1] != "X" else decrypted[:-1] 

text = "HELLO" 
key = "4321" 
cipher_text = row_column_transposition(text, key)  
print("Cipher text: ", cipher_text)  
text = row_column_transposition_decrypt(cipher_text, key)  
print("Decrypted text: ", text)  
