class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        x = str(x)
        size = len(x)
        odd = 0
        if size % 2 != 0:
            odd = 1
        for i in range(int(size / 2)):
            if x[int(size / 2) - 1 - i] != x[int(size / 2) + odd + i]:
                return False
        return True
