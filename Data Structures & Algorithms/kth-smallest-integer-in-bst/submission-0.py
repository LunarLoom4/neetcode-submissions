# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        value = 9999999999999999999
        count = 0
        def actualAlgo(root, k):
            nonlocal count, value   # Use 'nonlocal' when reassigning immutable variables inside a nested function.
            if not root:
                return None

            actualAlgo(root.left, k)
            if count < k:
                count += 1
                value = root.val
            actualAlgo(root.right, k)
        
        actualAlgo(root, k)
        return value

