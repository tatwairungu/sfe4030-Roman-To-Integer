# This test verifies that the converter correctly handles repeated Roman numeral characters.
# In the string "II":
#   - Both characters represent the same value ('I' = 1).
#   - Since Roman numerals allow up to three consecutive identical symbols (like II or III),
#     the algorithm should add them together.
# Therefore, 1 + 1 = 2.
# This test ensures that the converter correctly applies the additive rule for repetitions.

from romanToInteger import RomanNumeral
r = RomanNumeral()

def test_repetition_II():
    assert r.roman_to_int("II") == 2