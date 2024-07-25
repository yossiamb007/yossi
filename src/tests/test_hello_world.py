import os


def test_hello_word():
    my_var_value = os.getenv('USER_NAME')
    print(my_var_value)
    assert 1 == 1
