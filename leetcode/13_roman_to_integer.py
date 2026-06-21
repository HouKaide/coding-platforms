class Solution:
    def romanToInt(self, s: str) -> int:
        ROMAN_TO_INTEGER = {
            "M": 1000,
            "CM": 900,
            "D": 500,
            "CD": 400,
            "C": 100,
            "XC": 90,
            "L": 50,
            "XL": 40,
            "X": 10,
            "IX": 9,
            "V": 5,
            "IV": 4,
            "I": 1,
        }
        idx = 0
        final_num = 0
        while idx < len(s):
            if (idx < (len(s) - 1)) and (f"{s[idx]}{s[idx + 1]}" in ROMAN_TO_INTEGER.keys()):
                final_num += ROMAN_TO_INTEGER[f"{s[idx]}{s[idx + 1]}"]
                idx += 2
            else:
                roman_num = s[idx]
                final_num += ROMAN_TO_INTEGER[roman_num]
                idx = idx + 1
        return final_num
