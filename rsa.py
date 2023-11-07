def mod_inverse(a, m): # Function to calculate the modular inverse using extended Euclidean algorithm
    m0 = m  # Assigned the value of m to m0.
    y, x = 0, 1 # Declaration of variables.

    if m == 1:  # Condition whether m equals to 1 or not.
        return 0 # Returns Zero.

    while a > 1: # Condition to check a whether a is greater then 1 or not.
        q = a // m
        a, m = m, a % m
        x, y = y, x - q * y

    if x < 0:  # Condition to check x is negative or not.
        x += m0 # Increment the value of x bY m0.
    return x   # Returns the value of x.

def rsa_encrypt(M, public_key): # Function to perform RSA encryption using C = P^e mod n.
    e, n = public_key
    ciphertext = ((pow(M,e))%(n))
    return ciphertext # Returns the ciphertext.

def rsa_decrypt(ciphertext, private_key): # Function to perform RSA decryption using Plaintext = C^d mod n.
    d, n = private_key
    decrypted = ((pow(ciphertext,d))%n)
    return decrypted # Returns the value of rsa_decrypt.

def main():
    e_a = int(input("Enter Party A's public key 'e': "))  # Input Party A's public key.
    n_a = int(input("Enter Party A's n: "))
    public_key_a = (e_a, n_a)

    e_b = int(input("Enter Party B's public key 'e': "))  # Input Party B's public key.
    n_b = int(input("Enter Party B's n: "))
    public_key_b = (e_b, n_b)

    p_a = int(input("Enter prime number p for Party A: ")) # Input prime numbers p and q for Party A.
    q_a = int(input("Enter prime number q for Party A: "))
    phi_n_a = (p_a - 1) * (q_a - 1) # Arithmetic expression for finding the value of phi_n_a.
    d_a = mod_inverse(e_a, phi_n_a)
    private_key_a = (d_a, n_a)

    p_b = int(input("Enter prime number p for Party B: "))  # Input prime numbers p and q for Party B.
    q_b = int(input("Enter prime number q for Party B: "))
    phi_n_b = (p_b - 1) * (q_b - 1) # Arithmetic expression for finding the value of phi_n_b.
    d_b = mod_inverse(e_b, phi_n_b)
    private_key_b = (d_b, n_b)

    M_a_to_b = int(input("Enter the value of M (message) sent from A to B: "))  # Input value of M for encryption from A to B
    cipher_a_to_b = rsa_encrypt( M_a_to_b, public_key_b)
    decrypted_b = rsa_decrypt(cipher_a_to_b, private_key_b) # Assigning the value of rsa_decrypt method by calling it to decrypt_a.

    M_b_to_a = int(input("Enter the value of M (message) sent from B to A: "))  # Input value of M for encryption from B to A
    cipher_b_to_a = rsa_encrypt( M_b_to_a, public_key_a)
    decrypted_a = rsa_decrypt(cipher_b_to_a, private_key_a) # Assigning the value of rsa_decrypt method by calling it to decrypt_a.

    # Print the Answers of the following problems.
    print("Answers:")
    print("a. p_A =", p_a, "q_A =", q_a, "ϕ(n_A) =", phi_n_a, "public key for Party A =", public_key_a)
    print("b. Private key for Party A =", d_a)
    print("c. p_B =", p_b, "q_B =", q_b, "ϕ(n_B) =", phi_n_b, "public key for Party B =", public_key_b)
    print("d. Private key for Party B =", d_b)
    print("e. Cipher-text sent by A to B:", cipher_a_to_b)
    print("f. B decrypts:", decrypted_b)
    print("g. Cipher-text sent by B to A:", cipher_b_to_a)
    print("h. A decrypts:", decrypted_a)

if __name__ == "__main__":
    main()
