## Binary Search Tree

Write a function, build, that takes one parameter, A, a sorted array/list of strings.  It should return the root of a BST containing all the keys in A that is balanced.

    class TreeNode
    {
         string key;
         TreeNode left, right;
         TreeNode(string k, TreeNode L, TreeNode R) {key=k; left=L; right=R;}
    }
    
    TreeNode build(string A[])
    {
        if len(A) == 0:
            return None
            if len(A) == 1:
        return TreeNode(A[0])
        mid = (len(A) - 1) // 2
        root = TreeNode(A[mid])
        root.left = build(A[0:mid])
        root.right = build(A[mid+1:])
        return root
    }
    
    string A[] = {“A” “B”,”C”,”D”,”E”,”F”,”G”,”H”,”I”,”J”,”K”,”L”,”M”,”N”,”O”,”P”};
    TreeNode root = build(A);


