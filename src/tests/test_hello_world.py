def test_hello_word():
    import os
    my_var_value = os.getenv('USER_NAME')
    print(my_var_value)
    assert my_var_value is "yossi"
