import random  # Implements numbers, letters and symbols generators to a vast situations
import string  # Implements common operations to strings


passwdlength = 26
chars = string.ascii_letters + string.digits + 'ç!@#$%&*|,._-=+'

# print(chars)

rand = random.SystemRandom()

password = ''.join(rand.choice(chars)for i in range(passwdlength))

print(password)
