import string
import random

def password_generated():
    password = ''
    for i in range(12):
        password += random.choice(string.ascii_letters + string.digits)
    return password

print(password_generated())