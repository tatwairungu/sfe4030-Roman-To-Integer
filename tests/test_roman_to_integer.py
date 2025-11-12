import pytest
from romanToInteger import RomanNumeral

converter = RomanNumeral()

@pytest.mark.parametrize("roman, expected", [
    ("I", 1),
    ("V", 5),
    ("X", 10),
    ("L", 50),
    ("C", 100),
    ("D", 500),
    ("M", 1000),
    ("IV", 4),
    ("IX", 9),
    ("LVIII", 58),
    ("MCMXC", 1990),
    ("MCMXCIV", 1994),
])
def test_roman_to_int(roman, expected):
    assert converter.roman_to_int(roman) == expected