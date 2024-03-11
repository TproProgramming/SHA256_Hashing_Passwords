import hashlib

def hash_password(password):
    #Hash the password using Secure Hasing Algorithm 256-bit
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password
    
password = input("Enter your password to be hashed: ")
hashed_password = hash_password(password)
print(f"Hashed Password: {hashed_password}") 