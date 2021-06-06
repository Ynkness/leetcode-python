class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 最终还不是很懂，需要额外学习一下这个二叉树
# 二叉树中序遍历
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        stack = []
        if root:
            stack.append(root)
        while stack:
            node = stack[-1]
            if node:
                stack.pop()
                if node.right:
                    stack.append(node.right)
                stack.append(node)
                stack.append(None)
                if node.left:
                    stack.append(node.left)
            else:
                stack.pop()
                node = stack.pop()
                res.append(node.val)
        return res

root = [1,null,2,3]