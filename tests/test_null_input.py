from romanToInteger import RomanNumeral
r = RomanNumeral()

def test_empty_string_returns_zero_current_impl():
    assert r.roman_to_int("") == 0