import secrets
import string

def generate_password(length=10):
<<<<<<< HEAD
    characters = string.ascii_letters + string.digits + string.punctuation
=======
    characters = string.ascii_letters + string.digits
>>>>>>> ba9e2b96270d4845bf6e7e5471af3e2e98c13b20
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

# Usage example

