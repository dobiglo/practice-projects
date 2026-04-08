import random
import string

def generate_password(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    password=""
    for _ in range(length):
        password+=random.choice(chars)
    return password

print("Hello! Welcome to Password Generator!")
leng=int(input("Choose the length of the password (default is 12): ") or 12)
password=generate_password(leng)
print(f'Your generated password is: {password}')