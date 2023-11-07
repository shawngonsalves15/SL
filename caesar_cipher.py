def caesar_encrypt(plaintext, shift):
    encrypted_text = ""
    for char in plaintext:
        if char.isalpha():
            if char.isupper():
                encrypted_char = chr((ord(char) - 65 + shift) % 26 + 65)
            else:
                encrypted_char = chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            encrypted_char = char
        encrypted_text += encrypted_char
    return encrypted_text

def caesar_decrypt(ciphertext, shift):
    return caesar_encrypt(ciphertext, shift)

def main():
    try:
        choice = input("Enter 'E' for encrypt or 'D' for decrypt: ")
        message = input("Enter the message: ")
        shift = int(input("Enter the shift value + for encrypt - for decrypt: "))

        if choice.upper() == 'E':
            result = caesar_encrypt(message, shift)
            result = result.upper()
        elif choice.upper() == 'D':
            result = caesar_decrypt(message, shift)
            result = result.lower()
        else:
            print("Invalid choice. please enter the right choice.")
            return

        print("Result: ", result)
        
    except ValueError:
        print("Enter numeric value for shift.")

if __name__=="__main__":
    main()
        
    
