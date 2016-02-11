import random
import string
import time

SIZE = 8


def generate_key():
    random_key = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(SIZE))
    random_key = random_key[SIZE/2:] + '-' + random_key[:SIZE/2]
    return random_key


def get_current_date_formated():
    return time.strftime("%y/%m/%d - %H:%M:%S")