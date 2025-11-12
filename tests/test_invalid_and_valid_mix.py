import pytest
from romanToInteger import RomanNumeral
r = RomanNumeral()

def test_invalid_and_valid_mix_XIZ_raises():
    with pytest.raises(KeyError):
        r.roman_to_int("XIZ")