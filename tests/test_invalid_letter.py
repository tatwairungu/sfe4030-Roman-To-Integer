import pytest
from romanToInteger import RomanNumeral
r = RomanNumeral()

def test_invalid_letter_Z_raises():
    with pytest.raises(KeyError):
        r.roman_to_int("Z")