import random
import string

def generate_strong_password(length=16):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Example usage:
strong_password = generate_strong_password()
print("Strong password:", strong_password)
