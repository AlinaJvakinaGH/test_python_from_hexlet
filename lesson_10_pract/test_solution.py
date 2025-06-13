from pathlib import Path

from lesson_10_pract.functions import get_function

# функция, которую нужно протестировать
to_html_list = get_function()


# BEGIN (write your solution here)
def get_test_data_path(filename):
    return Path(__file__).parent / "test_data" / filename


def read_file(filename):
    return get_test_data_path(filename).read_text()

def test_csv():
    expected = read_file("result.html")
    path = get_test_data_path("list.csv")
    actual_1 = to_html_list["right"](path)
    actual_2 = to_html_list["fail1"](path)
    actual_3 = to_html_list["fail2"](path)
    actual_4 = to_html_list["fail3"](path)

    assert actual_1 == expected
    assert actual_2 == expected
    assert actual_3 == expected
    assert actual_4 == expected
