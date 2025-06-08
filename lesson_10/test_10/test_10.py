def test_txt():
    with_txt_path = "lesson_10/result.txt"
    with open(with_txt_path) as f:
        string = f.read()
    return string[::-1]