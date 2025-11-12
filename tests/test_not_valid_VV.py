import pytest
from romanToInteger import RomanNumeral
r = RomanNumeral()

@pytest.mark.xfail(reason="VV is invalid in strict Roman numerals; current impl returns 10")
def test_not_valid_double_VV_behaviour_current_impl():
    assert r.roman_to_int("VV") == 10