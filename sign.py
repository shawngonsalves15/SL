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

def rsa_sign(value_m,value_e,value_n): # function that calculate sign value and return.
    M_v = value_m
    E_v = value_e
    N_v = value_n
    S = ((pow(M_v,E_v))%(N_v)) # Formula of the sign value.
    return S

def rsa_verify(M_ver,E_ver,N_ver,S_ver): # Function that calculate the value of M' and returns the value.
    M_verify = M_ver
    E_verify = E_ver
    N_verify = N_ver
    S_verify = S_ver
    M2 = ((pow(S_verify,E_verify))%(N_verify)) # Formula to calculate M'.
    return M2

if __name__ == "__main__": # Main Function.
    p = int(input("Enter the value of p, such that value cannot be random, they should satisfy criteria as per RSA algorithm: "))
    q = int(input("Enter the value of q, such that value cannot be random, they should satisfy criteria as per RSA algorithm: "))
    e = int(input("Enter the value of e, such that value cannot be random, they should satisfy criteria as per RSA algorithm: "))
    n = p*q
    public_key = (e, n) # Assigning public key.
    print("Public Key:", public_key)
    phi_n = (p-1)*(q-1)
    d = mod_inverse(e,phi_n)
    private_key = (d,n)
    print("Private Key:", private_key)
    M = int(input("Enter the value of M (message): "))
    sign_value = rsa_sign(M,d,n) # function call of rsa_sign and assigning the value to the variable. 
    print("Sign Value of S: ", sign_value)
    print("-------------- Verification part --------------")
    M1 = int(input("Enter the value of M (message) to verify: "))
    S1 = int(input("Enter the value of S to verify: "))
    val = rsa_verify(M1,e,n,S1) # function call of rsa_verify and assigning the value to the variable. 
    if(val == M1):
        print("“The message is authenticate”")
    else:
        print("“Message is altered. Discard.”")
    

     
     
