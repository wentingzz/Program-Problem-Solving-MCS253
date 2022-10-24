class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(node):
            if not node:
                return 0
            nonlocal res
            l, r, leftEqual, rightEqual = dfs(node.left), dfs(node.right), (node.left and node.left.val == node.val), (
                        node.right and node.right.val == node.val)

            res = max(res, l, r)
            l = l + 1 if leftEqual else 0
            r = r + 1 if rightEqual else 0
            res = max(res, l + r)
            return max(l, r)

        dfs(root)
        return res