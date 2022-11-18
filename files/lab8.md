## General Problem Description 
Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:
- Insert a character 
- Delete a character 
- Replace a character
## Sample Input
    Input: word1 = "horse", word2 = "ros"
Output: 3

Explanation: 

    horse -> rorse (replace 'h' with 'r')
    rorse -> rose (remove 'r')
    rose -> ros (remove 'e')

    Input: word1 = "intention", word2 = "execution"
Output: 5

Explanation: 

    intention -> inention (remove 't')
    inention -> enention (replace 'i' with 'e')
    enention -> exention (replace 'n' with 'x')
    exention -> exection (replace 'n' with 'c')
    exection -> execution (insert 'u')
## Proposed Algorithm
### Description:

- Keep track of replace/delete/insert in a matrix. If delete, move to next char in word1. If insert, move to next char in word2. If replace, move to next char in both strings. If character of word 1 = character of word2, then we can move next character without replacement.
- Iteratively call insert/delete/replace on word1 and take the min, store the min in the matrix
## Edge Cases:
Input: word1 = "h", word2 = "ros"
Output: 3

Input: word1 = "hey", word2 = "yeh"
Output: 2

Input: word1 = “”, word2 = “hi”
Output: 2

Input: word1 = “happy”, word2 = “”
Output: 5

## Test Cases:
Input: word1 = “oxymoron”, word2 = “moron”
Output: 3
## Complexity:
- Time = O(N*M)
- Space = O(N*M)
## Implementation of Algorithm
Note: Don’t actually need to edit word1. Just need to count the number of steps. 

    int insert(word1, word2, matrix, i, j) {
        Return matrix[i][j - 1] + 1;
    }
    
    Int delete(word1, word2, matrix, i, j) {	
        j -= 1;
        Return matrix[i - 1][j] + 1;
    }
    
    Int replace(word1, word2, matrix, i, j) {
        // replace
        if word1[i] == word2[j]{
            return matrix[i-1][j-1]
        }
        else{
            return matrix[i-1][j-1] + 1
        }
    }
    
    Int minDistance(word1, word2) {
        Define matrix;
        for i in len(word1){
            for j in len(word2){
                matrix[i][j] = min(insert(word1, word2, matrix, i,j), delete(word1, word2, matrix,i,j), replace(word1, word2, matrix, i, j))
            }
        }
    }
## Advantages
O(N * M) runtime, O(N * M) space 

