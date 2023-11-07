def vigenera_cipher(text, key, mode):
    result = ""
    key = key.upper()
    key_index = 0
    for char in text:
        if char.isalpha():
            shift = ord(key[key_index]) - ord('A')
            if mode.upper() == 'D':
                shift = -shift

            if char.isupper():
                result += chr((ord(char) - 65 + shift) % 26 + 65)
            else:
                result += chr((ord(char) - 97 + shift) % 26 + 97)

            key_index = (key_index + 1) % len(key)
        else:
            result += char
    return result

def main():
    try:
        choice = input("Enter 'E' for encrypt or 'D' for decrypt: ").upper()
        message = input("Enter the message: ")
        key = input("Enter the key: ")

        if not key.isalpha():
            print("Invalid key. Only letters are allowed in the key.")
            return

        if choice.upper() == 'E':
            result = vigenera_cipher(message, key, choice)
            print("Encrypted text: ",result)
        else:
            result = result = vigenera_cipher(message, key, choice)
            print("Decrypted text: ",result)
    except ValueError:
        print("Invalid choice")

if __name__=="__main__":
    main()
