# This test verifies that each individual Roman numeral character 
# is correctly mapped to its corresponding integer value.
# These single-character numerals form the base of all Roman numbers:
#   I → 1, V → 5, X → 10, L → 50, C → 100, D → 500, M → 1000
#
# The test uses pytest’s parameterization to check all seven basic symbols 
# in one concise test function. If any mapping is wrong, it means the 
# core lookup dictionary in the converter is incorrect.

import pytest
from romanToInteger import RomanNumeral

r = RomanNumeral()

@pytest.mark.parametrize("s, expected", [
    ("I", 1), ("V", 5), ("X", 10), ("L", 50), ("C", 100), ("D", 500), ("M", 1000)
])
def test_single_letters(s, expected):
    assert r.roman_to_int(s) == expected