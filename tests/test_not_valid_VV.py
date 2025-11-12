# This test examines how the converter handles an invalid Roman numeral pattern "VV".
# In the rules of Roman numerals, 'V' (5) should never be repeated — writing "VV" is invalid.
# However, the current implementation does not perform strict validation;
# it simply adds the two values together (5 + 5 = 10).
# Therefore, this test uses pytest.mark.xfail to indicate that it is an *expected failure*:
# the implementation returns 10 even though "VV" is not a valid Roman numeral.
# This helps document the current behavior and signals that validation could be improved later.

import pytest
from romanToInteger import RomanNumeral
r = RomanNumeral()

@pytest.mark.xfail(reason="VV is invalid in strict Roman numerals; current impl returns 10")
def test_not_valid_double_VV_behaviour_current_impl():
    assert r.roman_to_int("VV") == 10