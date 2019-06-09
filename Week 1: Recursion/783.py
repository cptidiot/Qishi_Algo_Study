'''
Runtime: 36 ms, faster than 91.79% of Python3 online submissions for Minimum Distance Between BST Nodes.
Memory Usage: 13.2 MB, less than 52.97% of Python3 online submissions for Minimum Distance Between BST Nodes.
'''

class Solution:
    pre = -float('inf')
    res = float('inf')
    def minDiffInBST(self, root: TreeNode) -> int:
        if root is None:
            return
        
        self.minDiffInBST(root.left)
        self.res = min(self.res, root.val-self.pre)
        self.pre = root.val
        self.minDiffInBST(root.right)
        return self.res
            
            