from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)   # Eating Speed Range

        while low <= high:
            mid = (low + high) // 2

            if self.func(mid, piles) > h:
                low = mid + 1
            else:                   # Eating Speed 'mid' might lead to an eating time less than 'h', say 'h1', but it is possible that an even lower eating speed might still give an eating time less than 'h', say 'h2' where h1 <= h2 < h.
                                    #   ''     ''  'mid' might also lead to an eating time equal to 'h', but it is possible that an even lower eating speed also give the same eating time 'h' (cannot be lower as decreasing the eating speed cannot reduce the eating time).
                high = mid - 1

        return low
    
    def func(self, speed: int, piles: List[int]) -> int:
        count = 0
        for num in piles:
            count += (num + speed - 1) // speed     # No. of hours required to eat the pile at given 'speed'.
        return count

