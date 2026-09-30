# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value

class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self.quickSortAlgo(pairs, 0, len(pairs) - 1)
        return pairs

    def quickSortAlgo(self, arr: List[Pair], s: int, e: int) -> None:
        # Base Case: Lone element is handled by it
        if e - s <= 0:
            return arr
        
        pivot = arr[e]      # 'pivot' denotes the last element of the array
        left = s            # 'left' pointer gives the position for the swapping position

        # Swap all element which are smaller than the 'pivot' on the left side of the array
        for i in range(s, e):      # Starting from 's'; Going till 'e - 1'
            if arr[i].key < pivot.key:
                tmp = arr[i]
                arr[i] = arr[left]
                arr[left] = tmp
                left += 1
        
        # Swap the pivot element with the element at the 'left' pointer
        arr[e] = arr[left]
        arr[left] = pivot

        # Quick sort left side of the pivot
        self.quickSortAlgo(arr, s, left - 1)

        # Quick sort right side of the pivot
        self.quickSortAlgo(arr, left + 1, e)
