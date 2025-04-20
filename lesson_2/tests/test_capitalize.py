from lesson_2.pkg.capitalize import capitalize

assert capitalize("") == ""
assert capitalize("hello") == "Hello"
assert capitalize(None) == "Пишите буквами"
assert capitalize(int) == "Пишите буквами"

print('Все тесты пройдены!')