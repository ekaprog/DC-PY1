from random import sample
import string


def get_random_password(number_of_symbols=8) -> str:
    pool = [symb for symb in ''.join([string.ascii_uppercase, string.ascii_lowercase, string.digits])]
    password = ''.join(sample(pool, number_of_symbols))

    return password


print(get_random_password())
