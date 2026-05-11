# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if (not preorder):
            return None
        
        root = TreeNode(preorder[0])
        rootInOrderIdx = inorder.index(root.val)

        leftSubtreePreorder = preorder[1:rootInOrderIdx + 1]
        leftSubtreeOrder = inorder[0:rootInOrderIdx]

        root.left = self.buildTree(leftSubtreePreorder, leftSubtreeOrder)

        rightSubtreePreorder = preorder[rootInOrderIdx + 1:]
        rightSubtreeOrder = inorder[rootInOrderIdx + 1:]

        root.right = self.buildTree(rightSubtreePreorder, rightSubtreeOrder)

        return root