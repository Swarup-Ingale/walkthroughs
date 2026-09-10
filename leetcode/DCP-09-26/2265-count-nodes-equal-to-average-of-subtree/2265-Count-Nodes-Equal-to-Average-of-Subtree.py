# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.result = 0

        def dfs(node):
            if not node:
                return 0, 0

            left_sum, left_count = dfs(node.left)
            right_sum, right_count = dfs(node.right)

            curr_sum = left_sum + right_sum + node.val
            curr_count = left_count + right_count + 1

            if curr_sum // curr_count == node.val:
                self.result += 1

            return curr_sum, curr_count

        dfs(root)
        return self.result