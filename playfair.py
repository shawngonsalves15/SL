def prepare_text(text): # Function to prepare the text for encryption by removing spaces and converting to uppercase
    text = text.replace(" ", "").upper()
    text = text.replace("J", "I") # Replace J (I and J are usually treated as the same in Playfair cipher)
    return text

def create_playfair_matrix(key): # Function to create the Playfair matrix based on the key
    key = prepare_text(key)
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # Note: We skip 'J' in the alphabet
    matrix = []

    for char in key + alphabet:
        if char not in matrix: # Condition to check whether character is already present or not.
            matrix.append(char)

    playfair_matrix = [matrix[i:i+5] for i in range(0, 25, 5)] # Create a 5x5 Playfair matrix by splitting the 'matrix' list into rows of 5 elements each

    return playfair_matrix  # Returns the playfair_matrix

def find_char_position(matrix, char): # Function to find the position of a character in the Playfair matrix
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return i, j

def playfair_encrypt(plain_text, key): # Function to encrypt using the Playfair cipher
    playfair_matrix = create_playfair_matrix(key)
    plain_text = prepare_text(plain_text) # Calling function prepare_text
    encrypted_text = ""

    i = 0
    while i < len(plain_text):
        char1 = plain_text[i]
        char2 = plain_text[i + 1] if i + 1 < len(plain_text) else 'X'

        row1, col1 = find_char_position(playfair_matrix, char1)
        row2, col2 = find_char_position(playfair_matrix, char2)# Find the position of 'char2' in the Playfair matrix for encryption/decryption

        if row1 == row2:
            col1 = (col1 + 1) % 5
            col2 = (col2 + 1) % 5
        elif col1 == col2:
            row1 = (row1 + 1) % 5
            row2 = (row2 + 1) % 5
        else:
            col1, col2 = col2, col1

        encrypted_text += playfair_matrix[row1][col1] + playfair_matrix[row2][col2] # Add the encrypted pair of characters to the 'encrypted_text'

        i += 2

    return encrypted_text

def playfair_decrypt(cipher_text, key): # Function to decrypt using the Playfair cipher
    playfair_matrix = create_playfair_matrix(key)
    cipher_text = prepare_text(cipher_text)
    decrypted_text = ""

    i = 0
    while i < len(cipher_text):
        char1 = cipher_text[i]
        char2 = cipher_text[i + 1]

        row1, col1 = find_char_position(playfair_matrix, char1)
        row2, col2 = find_char_position(playfair_matrix, char2)

        if row1 == row2:
            col1 = (col1 - 1) % 5
            col2 = (col2 - 1) % 5
        elif col1 == col2:
            row1 = (row1 - 1) % 5
            row2 = (row2 - 1) % 5
        else:
            col1, col2 = col2, col1

        decrypted_text += playfair_matrix[row1][col1] + playfair_matrix[row2][col2] # Add the decrypted pair of characters to the 'decrypted_text'

        i += 2

    return decrypted_text # Returns decrypted text

def main(): # main function
    print("Playfair Cipher")
    choice = input("Enter 'E' to encrypt or 'D' to decrypt: ").upper() # Enter choice E for encryption, D for decryption.

    if choice not in ['E', 'D']: # Condition check in matrix
        print("Invalid choice. Please enter 'E' or 'D'.") 
        return

    key = input("Enter the key: ") # Taking key input from the user.
    text = input("Enter the text: ") # Taking text input from the user.

    if choice == 'E': 
        result = playfair_encrypt(text, key) # Calling function playfair encrypt
        print("Encrypted Text:", result)
    elif choice == 'D':
        result = playfair_decrypt(text, key) # Calling Function playfair decrypt
        print("Decrypted Text:", result)
    else:
        print("Invalid choice.")

    playfair_matrix = create_playfair_matrix(key) # Calling playfair matrix 
    print("Playfair Matrix:")
    for row in playfair_matrix:
        print(" ".join(row))

if __name__ == "__main__":
    main()
