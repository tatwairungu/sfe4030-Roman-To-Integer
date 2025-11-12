# This test verifies that when the first Roman numeral has a greater value 
# than the next one (e.g., 'V' = 5 and 'I' = 1 in "VI"), 
# the algorithm correctly adds both values (5 + 1 = 6) instead of applying subtraction.
# It ensures normal additive behavior is handled correctly.

from romanToInteger import RomanNumeral
r = RomanNumeral()

def test_first_number_bigger_than_next_VI():
    assert r.roman_to_int("VI") == 6