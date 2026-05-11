# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indices = {val: idx for idx, val in enumerate(inorder)}

        preIdx = 0
        # l, r: current subarray of inorder
        def dfs(l, r):
            nonlocal preIdx
            
            if l > r:
                return None
            
            root = TreeNode(preorder[preIdx])
            preIdx += 1

            rootInorderIdx = indices[root.val]

            root.left = dfs(l, rootInorderIdx-1)
            root.right = dfs(rootInorderIdx+1, r)

            return root

        return dfs(0, len(inorder)-1)