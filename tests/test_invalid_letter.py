# This test verifies that the converter correctly handles completely invalid Roman numerals.
# In this case, the input "Z" is not a valid Roman numeral character and is not present 
# in the Roman numeral map. The function is expected to raise a KeyError when it tries 
# to look up 'Z' in the map. 
# This ensures that the implementation does not silently accept or convert invalid inputs.

import pytest
from romanToInteger import RomanNumeral
r = RomanNumeral()

def test_invalid_letter_Z_raises():
    with pytest.raises(KeyError):
        r.roman_to_int("Z")