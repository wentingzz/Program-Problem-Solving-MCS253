## General Problem Description
Leetcode 687:

Given the root of a binary tree, return the length of the longest path, where each node in the path has the same value. This path may or may not pass through the root.

The length of the path between two nodes is represented by the number of edges between them.

## Sample Input

Input: root = [5,5,5,5,1,null,5]
Output: 4

## Proposed Algorithm
### Description:
1. We use depth first search to iterate through the tree. 
2. When we reach the leaf node, we return (node.val, 0)
3. When left child and right child return their values, parent will do the following:
   1. if parent.val is not equal to any of its children, we update the global res variable and return (parent.val, 0)
   2. if parent val is the same as the value of its left and right child 
      1. we calculate the path passing this node including its left and right child, and update the global res variable if the new path is greater. 
      2. we compare the path returned by the child and get the one with greater value. return it as (parent.val, greatedReturnedPath + 1)
   3. If only one of the child has the same value as the parent. We return (parent.val, childReturned + 1)

4. In the end, we update the global res and return after the dfs search.


## Edge Cases:
Input: root = []
Output: 0

Input: root = [1]
Output: 0

input: root = [4,4,4,4,4,null,5]
Output: 3

Input: root = [5,4,5,1,1,null,5]
Output: 2

Input: root = [5,4,3,2,1,null,5]
Output: 0

## Complexity:
- Time = O(Edges) 
- Space = O(1)

## Implementation of Algorithm

    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
            res = 0
        
        def dfs(node):
            if not node:
                return (0,0)
            if node.isLeaf():
                return (node.val,0)
            
            leftreturned = dfs(node.left)
            rightreturned = dfs(node.right)
            res = max(res, leftreturned[1], rightreturned[1])

            if parent.val != children.val:
                return (parent.val,0)
            if parent.val = left.val = right.val:
                res = max(res, leftreturned[1] + 1 + rightreturned[1] + 1)
                leftreturned[1] > rightreturned[1]:
                    return (parent.val, leftreturned[1] + 1)
                else:
                    (parent.val, rightreturned[1] + 1)
            elif parent.val == left.val:
                return (parent.val, leftreturned[1] + 1)
            elif parent.val = right.val:
                return (parent.val, rightreturned[1] + 1)
        res = max(res, dfs(root)[1])
        return res


## Advantages
Advantages: it’s a one-pass and does not take up extra storage with the use of a global result value updates with max(result, returned)
