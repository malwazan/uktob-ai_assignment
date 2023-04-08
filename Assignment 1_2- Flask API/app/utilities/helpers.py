import os
import random
import string
    

def generate_random_string(n):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for i in range(n))


def is_float(number):
    try:
        float(number)
        return True
    except ValueError:
        return False