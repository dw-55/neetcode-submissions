import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        left = 1
        right = max(piles)
        minimum = right

        while left <= right:
            mid = (right + left)//2
            curr = 0
            for i in range(len(piles)):
                curr += math.ceil(piles[i]/mid)
                
            if curr <= h:
                minimum = min(mid, minimum)
                right = mid - 1
            else:
                left = mid + 1
        return minimum
