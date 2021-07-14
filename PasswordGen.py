from random import SystemRandom
from string import ascii_letters , digits, punctuation
length = 200


def PasswordGen(length):
    global password
    symbols = ascii_letters + digits + punctuation
    print(symbols)
    password = "".join(SystemRandom().choice(symbols)for i in range(length))

PasswordGen(200)
print(password)
