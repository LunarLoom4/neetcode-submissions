# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value

class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        if len(pairs) > 1:
            # Divides the array into two halves
            left_arr = pairs[: len(pairs) // 2]
            right_arr = pairs[len(pairs) // 2 :]

            # Recursion Step: Sorts the left_arr and right_arr
            self.mergeSort(left_arr)
            self.mergeSort(right_arr)

            # Merge Step
            i = 0   # idx pointer for left_arr
            j = 0   # idx pointer for right_arr
            k = 0   # idx pointer for final merged array

            while i < len(left_arr) and j < len(right_arr):
                if left_arr[i].key <= right_arr[j].key:
                    pairs[k] = left_arr[i]
                    i += 1
                else:
                    pairs[k] = right_arr[j]
                    j += 1
                k += 1
            
            # For adding the portion of 'left_arr' that is left to be added to the final array
            while i < len(left_arr):
                pairs[k] = left_arr[i]
                i += 1
                k += 1

            # For adding the portion of 'right_arr' that is left to be added to the final array
            while j < len(right_arr):
                pairs[k] = right_arr[j]
                j += 1
                k += 1

        return pairs
