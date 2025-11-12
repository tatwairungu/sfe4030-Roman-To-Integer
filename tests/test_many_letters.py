# This test verifies that the converter correctly handles Roman numerals 
# composed of multiple valid characters that follow the additive rule.
# The input "XI" consists of:
#   - 'X' = 10
#   - 'I' = 1
# Since 'X' (10) is greater than 'I' (1), their values are simply added together (10 + 1).
# The expected result is 11.
# This ensures that multi-character numerals without subtractive notation are handled properly.

from romanToInteger import RomanNumeral
r = RomanNumeral()

def test_many_letters_XI():
    assert r.roman_to_int("XI") == 11