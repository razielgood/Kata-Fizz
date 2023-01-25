import unittest
class TestRomanNumerals(unittest.TestCase):
    def test_to_roman(self):
        self.assertEqual(to_roman(1), "I")
        self.assertEqual(to_roman(4), "IV")
        self.assertEqual(to_roman(9), "IX")
        self.assertEqual(to_roman(40), "XL")
        self.assertEqual(to_roman(90), "XC")
        self.assertEqual(to_roman(400), "CD")
        self.assertEqual(to_roman(1001), "MI")
        self.assertEqual(to_roman(3999), "MMMCMXCIX")
        

def to_roman(num):
    roman_dict = {
        1000: "M",
        900: "CM",
        500: "D",
        400: "CD",
        100: "C",
        90: "XC",
        50: "L",
        40: "XL",
        10: "X",
        9: "IX",
        5: "V",
        4: "IV",
        1: "I"
    }
    result = ""
    for value, letter in roman_dict.items():
        while num >= value:
            result += letter
            num -= value
    return result

if __name__ == "__main__":
    unittest.main()

