from romanToInteger import RomanNumeral
r = RomanNumeral()

def test_many_letters_XI():
    assert r.roman_to_int("XI") == 11