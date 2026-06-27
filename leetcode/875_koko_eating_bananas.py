from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def hours_calc( mid):
            tmp = 0
            for pile in piles:
                val = (pile + mid -1) // mid
                tmp += val
            return tmp

        left, right = 1, max(piles)
        k = right
        while left <= right:
            mid = (left + right) // 2
            hours = hours_calc(mid)
            if hours <= h:
                k = mid
                right = mid - 1
            else:
                left = mid + 1
        return k