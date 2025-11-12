class RomanNumeral:
    # Static map equivalent
    map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    def roman_to_int(self, s: str) -> int:
        converted_number = 0
        for i in range(len(s)):
            current_number = self.map[s[i]]
            next_number = self.map[s[i + 1]] if i + 1 < len(s) else 0

            if current_number >= next_number:
                converted_number += current_number
            else:
                converted_number -= current_number

        return converted_number


if __name__ == "__main__":
    converter = RomanNumeral()
    print(converter.roman_to_int("XIV"))    # Expected 14
    print(converter.roman_to_int("MCMXC"))  # Expected 1990
    print(converter.roman_to_int("LVIII"))  # Expected 58