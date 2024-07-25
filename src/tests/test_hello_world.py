import os


def test_hello_word():
    my_var_value = os.getenv('USER_NAME')
    assert my_var_value == "yossi"
