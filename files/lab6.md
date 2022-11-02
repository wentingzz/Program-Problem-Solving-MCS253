## Leetcode 200: Number of Islands
## Sample Input
    Input: grid = [
      ["1","1","1","1","0"],
      ["1","1","0","1","0"],
      ["1","1","0","0","0"],
      ["0","0","0","0","0"]
    ]
Output: 1

    Input: grid = [
      ["1","1","0","0","0"],
      ["1","1","0","0","0"],
      ["0","0","1","0","0"],
      ["0","0","0","1","1"]
    ]
Output: 3

## Algorithm
### Description:
- Iterate through start of matrix 
  - If val == 1, check the top/bottom/left/right recursively 
    - If none of the checked values are land we’ve already checked, increment number of islands 
    - Set visited values to -1 
- In the end, return number of islands

## Edge Cases:
    grid = [[0]]
Output = 0

## Complexity:
- Time = O(N) where N = matrix Row * Column
- Space = O(1)

## Implementation of Algorithm
    def mark(r,c):
        if r is outOfBound or c is outOfBound or grid[r][c] != “1”:
            return
        grid[r][c] = “-1”
        mark(r+1, c)
        mark(r-1, c)
        mark(r, c+1)
        mark(r, c-1)
    count = 0
    for i in range(rowLength):
        for j in range(colLength):
            if grid[r][c] == “1”:
                mark(i,j)
                count = count + 1
    return count



## Disadvantages
Our algorithm requires editing the parameters, which may mess with testing a bit. 
