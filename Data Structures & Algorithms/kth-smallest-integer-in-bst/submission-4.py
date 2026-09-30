# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        value = None
        count = 0
        def actualAlgo(root, k):
            nonlocal count, value
            if not root:
                return

            actualAlgo(root.left, k)
            if count < k:
                count += 1
                value = root.val
            if count == k:
                return      # Stops further recursion once we find the k-th element
            actualAlgo(root.right, k)

        actualAlgo(root, k)
        return value

