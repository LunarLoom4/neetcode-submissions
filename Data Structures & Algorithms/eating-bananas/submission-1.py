from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)  # Correct initialization of search range

        while low <= high:
            mid = (low + high) // 2  # Mid represents the eating speed

            if self.func(mid, piles) > h:  # Check if mid is too slow
                low = mid + 1
            else:  # Mid might be a valid answer, but try a smaller k
                high = mid - 1

        return low  # Minimum valid speed
    
    def func(self, speed: int, piles: List[int]) -> int:
        count = 0
        for num in piles:
            count += (num + speed - 1) // speed  # Ceiling division
        return count
