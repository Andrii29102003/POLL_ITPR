import secrets
import string

def generate_password(length=10):
    characters = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

# Usage example

