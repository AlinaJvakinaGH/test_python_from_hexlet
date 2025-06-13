import os
import re

import pytest
from generate_password.implementations import right
from generate_password.src import solution
from generate_password.implementations import wrong1
from generate_password.implementations import wrong2
from generate_password.implementations import wrong3


@pytest.fixture(name="generate_password")
def _generate_password():
    name = os.environ["FUNCTION_VERSION"]
    return {
        "user_implementation": solution,
        "right": right,
        "wrong1": wrong1,
        "wrong2": wrong2,
        "wrong3": wrong3,
    }[name].generate_password


def test_generate_password_min_len(generate_password):
    password = generate_password()
    assert len(password) == 5


# BEGIN (write your solution here)
def test_generate_password_min_len(generate_password):
    password = generate_password(include_uppercase=True, include_digits=True, include_special=True)
    assert re.search(r"[!\"#$%&'()*+,-./:;<=>?@[\\\]^_`{|}~]", password)
    assert re.search(r"[1234567890]", password)
    assert re.search(r"[A-Z]", password)
# END
