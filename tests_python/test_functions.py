from functions import *

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(10, 4) == 6

def test_multiply():
    assert multiply(3, 5) == 15

def test_divide():
    assert divide(10, 2) == 5

def test_divide_by_zero():
    import pytest
    with pytest.raises(ValueError):
        divide(10, 0)

def test_is_even_true():
    assert is_even(4) is True

def test_is_even_false():
    assert is_even(5) is False

def test_reverse_string():
    assert reverse_string("hello") == "olleh"

def test_capitalize_words():
    assert capitalize_words("hello world") == "Hello World"

def test_average():
    assert average([2, 4, 6]) == 4
