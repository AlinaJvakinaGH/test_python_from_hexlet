import random
import string

def generate_password(length=None, include_uppercase=True, include_digits=True, include_special=True):
    if length is None:
        length = 5

    characters = string.ascii_lowercase

    if include_uppercase:
        characters += string.ascii_uppercase

    if include_digits:
        characters += string.digits

    if include_special:
        characters += string.punctuation

    # Генерация пароля
    password = ''.join(random.choices(characters, k=length))

    return password
