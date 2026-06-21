from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        PHONE_CHARACTERS = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        answer = [""]
        for digit in digits:
            answer = [idx + ch for idx in answer for ch in PHONE_CHARACTERS[int(digit) - 2]]
        return answer