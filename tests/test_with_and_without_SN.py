# This test verifies that the converter correctly handles a Roman numeral
# that mixes both additive and subtractive notation in one sequence.
#
# In the numeral "XIV":
#   - 'X' = 10  → additive part
#   - 'I' = 1 and 'V' = 5  → subtractive pair ('IV' = 4)
# The total should therefore be 10 + 4 = 14.
#
# This test ensures that the converter can correctly process numerals
# that include both standard additions and a subtractive combination
# within the same string.

from romanToInteger import RomanNumeral
r = RomanNumeral()

def test_mixed_XIV():
    assert r.roman_to_int("XIV") == 14