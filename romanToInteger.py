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
        if not s:
            raise ValueError("Input cannot be empty.")

        # Ensure all characters are valid Roman numerals
        for ch in s:
            if ch not in self.map:
                raise ValueError(f"'{ch}' is not a valid Roman numeral symbol.")

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

    print("🧮 Roman Numeral Converter")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("Enter a Roman numeral: ").strip().upper()

        if user_input.lower() == "exit":
            print("Goodbye! 👋")
            break

        try:
            result = converter.roman_to_int(user_input)
            print(f"✅ {user_input} = {result}\n")
        except ValueError as e:
            print(f"❌ Error: {e}\n")