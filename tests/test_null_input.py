# This test checks how the converter handles an empty string input ("").
# In Roman numerals, an empty or null input technically has no meaning,
# but the current implementation returns 0 since the for-loop never runs
# (no characters to process, so the initialized converted_number = 0 is returned).
# This test ensures the function behaves predictably with empty input
# and does not crash or raise an unexpected error.

from romanToInteger import RomanNumeral
r = RomanNumeral()

def test_empty_string_returns_zero_current_impl():
    assert r.roman_to_int("") == 0