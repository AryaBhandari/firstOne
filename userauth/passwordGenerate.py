import random
import string

def generatePassword(l=10):
    letters=string.ascii_letters
    return ''.join(random.choice(letters) for i in range(l))
