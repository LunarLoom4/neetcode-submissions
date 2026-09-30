# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def minNode(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        curr = root
        while curr and curr.left:
            curr = curr.left
        return curr

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root == None:
            return None

        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if root.right == None:
                return root.left
            elif root.left == None:
                return root.right
            else:
                miniNode = self.minNode(root.right)
                root.val = miniNode.val
                root.right = self.deleteNode(root.right, miniNode.val)

        return root
