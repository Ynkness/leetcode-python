# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def fuc(left, right):
            if left and not right:
                return False
            elif right and not left:
                return False
            elif not left and not right:
                return True
            else:
                return left.val==right.val and fuc(left.left,right.right) and fuc(left.right,right.left)
        if not root:
            return True
        result=fuc(root.left,root.right)
        return result