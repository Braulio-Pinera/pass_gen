from generator.password_generator import (
    generate_password, 
    has_lowercase, 
    has_number, 
    has_symbol, 
    has_uppercase
)

from random import randint

def test_password_length():
    password = generate_password()
    assert len(password) == 12

def test_password_is_string():
    password = generate_password()
    assert isinstance(password, str)

def test_has_lowercase():
    assert has_lowercase("abc") is True

def test_has_lowercase():
    assert has_uppercase("ABC") is True

def test_has_number():
    assert has_number("abc123") is True

def test_has_symbol():
    assert has_symbol("abc!?") is True

def test_random_password_length():
    n = randint(1, 15)
    password = generate_password(n)
    assert len(password) == n

print("All tests completes succesfully")