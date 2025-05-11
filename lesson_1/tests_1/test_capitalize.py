from pkg.capitalize import capitalize

def test_capitalize():
    if capitalize('hello') != 'Hello':
        raise Exception('Бум! Произошла ошибка, останавливаемся')

    if capitalize('') != '':
        raise Exception('Бум! Произошла ошибка, останавливаемся')

    if capitalize(None) != 'Пишите буквами':
        raise Exception('Бум! Произошла ошибка, останавливаемся')

    if capitalize(3) != 'Пишите буквами':
        raise Exception('Бум! Произошла ошибка, останавливаемся')

print('Все тесты пройдены!')