# This test checks how the converter handles a mix of valid and invalid Roman numeral characters.
# In the string "XIZ":
#   - 'X' (10) and 'I' (1) are valid Roman numerals,
#   - but 'Z' is invalid and not present in the Roman numeral mapping.
# The current implementation raises a KeyError when an unknown symbol like 'Z' is encountered.
# This test ensures that such invalid characters correctly trigger an exception,
# preventing incorrect conversions or silent failures.

import pytest
from romanToInteger import RomanNumeral
r = RomanNumeral()

def test_invalid_and_valid_mix_XIZ_raises():
    with pytest.raises(KeyError):
        r.roman_to_int("XIZ")