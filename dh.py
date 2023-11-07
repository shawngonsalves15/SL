import math # Imported Maths Module.

def is_prime(num): # function to check prime or not.
    if num < 2:
        raise Exception("Please enter a prime number.") # Raise Exception if a number is not a prime number.
        exit()
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0: # Condition to check for prime 
            raise Exception("Please enter a prime number.")# Raise Exception if a number is not a prime number.
            exit()
            return False
    return True # function return value.

def is_primitive_root(alpha, q): #function to find primitive root or not.
    if math.gcd(alpha, q) != 1:
        return False
    values = set()
    for i in range(1, q):
        value = pow(alpha, i, q) # Using formula over here.
        if value in values:
            return False
        values.add(value) # adding value to values set.
    return True # Return the value of a function.

def find_primitive_roots(q): # function for creating an array of primitive roots.
    primitive_roots = []
    primitive_actual = []
    for alpha in range(2, q): # For loop begin for appending the value to an array.
        if is_primitive_root(alpha, q):
            primitive_roots.append(alpha) # append values over here.
    size = len(primitive_roots)
    for i in range(0,size): # for loop begin for only required primitive roots in an array.
        if(primitive_roots[i] <= q):
            primitive_actual.append(primitive_roots[i])
    return primitive_actual # Return the value of a function

def check_primitive(alpha,a): # function to whether user has entered proper primitive value or not.
    flag = False # created boolean variable.
    for i in range(0,len(alpha)):
        if( alpha[i] == a): #checking condition over here.
            flag = True
    if flag == False:
        raise Exception("Please enter a proper primitive root of q.")
        
def check_private(a): # function to check user entered private key is correct or not.
    if(a > q):
        raise Exception("Please enter the private key less than or equal to q.")

def public_key_generator(alpha,Private_key,q): # Functcion to calculate public key.
    a = alpha
    p = Private_key
    public_key = (pow(a,p)%q)
    return public_key

def secret_key_generator(public_key,private_key,q): # function to calculate secret key.
    pu = public_key
    pr = private_key
    key = (pow(pu,pr)%q)
    return key

def check_key(k1,k2): # verfication of secret key.
    if(k1 == k2):
        print("Alice and Bob communicate using the symmetric algorithm of their choice and the shared secret key.")
    else:
        print("Alice and Bob Can't communicate using the symmetric algorithm of their choice and the shared secret key.")
    

if __name__ == "__main__": # Main start over here.
    q = int(input("Enter the value of q, where q is a prime number: "))
    is_prime(q)
    alpha = find_primitive_roots(q)
    print(alpha)
    a = int(input("Enter the value of alpha, where alpha is a primitive root mod q: "))
    check_primitive(alpha,a)
    print("----------------- Private Keys -----------------")
    Private_key_a = int(input("Enter the private key of Alice, Where private key should be less than equal to q: "))
    check_private(Private_key_a)
    Private_key_b = int(input("Enter the private key of BoB, Where private key should be less than equal to q: "))
    check_private(Private_key_b)
    print("----------------- Private Keys -----------------")
    print("Private Key of Alice is: ",Private_key_a)
    print("Private Key of Bob is: ",Private_key_b)
    print("----------------- Public Keys -----------------")
    Public_key_a = public_key_generator(a,Private_key_a,q)
    print("Public key of Alice: ",Public_key_a)
    Public_key_b = public_key_generator(a,Private_key_b,q)
    print("Public key of Bob: ",Public_key_b)
    print("-------- Alice and Bob exchange their public key with each other --------")
    Public_a = Public_key_b
    Public_b = Public_key_a
    print("----------------- Secret Keys -----------------")
    secret_key_a = secret_key_generator(Public_a,Private_key_a,q)
    print("Secret key of Alice is: ",secret_key_a)
    secret_key_b = secret_key_generator(Public_b,Private_key_b,q)
    print("Secret key of Bob is: ",secret_key_b)
    print("----------------- Verfication start -----------------")
    check_key(secret_key_a,secret_key_b)
    
    
    
    
    
    
    
    
                  
