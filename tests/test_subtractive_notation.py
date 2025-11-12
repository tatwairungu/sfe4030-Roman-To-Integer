# This test verifies that the converter correctly applies the *subtractive notation* rule 
# used in Roman numerals. 
# In the numeral "IV":
#   - 'I' (1) appears before 'V' (5),
#   - meaning it should be subtracted rather than added (5 - 1 = 4).
# This rule is also used in other numerals like IX (9), XL (40), and CM (900).
# The test ensures that the converter correctly identifies and handles 
# this subtractive pattern, returning 4 as expected.

from romanToInteger import RomanNumeral
r = RomanNumeral()

def test_subtractive_IV():
    assert r.roman_to_int("IV") == 4