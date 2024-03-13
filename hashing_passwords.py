import hashlib
import secrets


def salt_password(password):
    #Generate a random salt
    salt = password + secrets.token_hex(16)
    return salt
    
def hash_password(salted_password):
    #Hash the password using Secure Hasing Algorithm 256-bit
    hashed_password = hashlib.sha256(salted_password.encode()).hexdigest()
    return hashed_password

def main():   
    password = input("Enter your password to be hashed: ")

    #Salt password
    salted_password = salt_password(password)

    #Create hashed password
    hashed_password = hash_password(salted_password)

    print(f"Plain Text Password: {password}")
    print(f"Salted Password {salted_password}") 
    print(f"Hashed Password: {hashed_password}")

if __name__ == "__main__":
    main()