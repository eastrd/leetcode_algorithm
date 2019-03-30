class Solution:
    def romanToInt(self, s: str) -> int:
        mapper = {
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900,
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        res = 0
        while s:
            if len(s) > 1 and s[:2] in mapper:
                res += mapper[s[:2]]
                s = s[2:]
            else:
                res += mapper[s[0]]
                s = s[1:]
        return res
