
from leapyear import is_leap_year

def test_leap_year():
    assert is_leap_year(2024) == True

def test_not_leap_year():
    assert is_leap_year(2025) == False

def test_century_not_leap_year():
    assert is_leap_year(1900) == False

def test_century_leap_year():
    assert is_leap_year(2000) == True
