text = 22

def capitalize(text=None):
    if text == "":
        return ""
    if text == None:
        return 'Пишите буквами'
    if text == int:
        return 'Пишите буквами'
    first_char = text[0].upper()
    rest_substring = text[1:]
    return f'{first_char}{rest_substring}'