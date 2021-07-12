# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        def helper(root):
            if not root:
                return 0
            left=helper(root.left)
            right=helper(root.right)
            # 左子树不平衡或者右子树不平衡
            if left is False or right is False:
                return False
            # 左右子树都平衡 此时left和right为左右子树的深度 判断root为根节点的子树是否平衡
            if abs(left-right)>1:
                return False 
            # 左右子树 和root为根节点的当前树 都平衡 返回root为根的树深度
            return max(left, right)+1
        if helper(root):
            return True
        else:
            return False