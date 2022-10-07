# Substring Finder Program

## Prompt
Create a program that takes a list of strings and, for each string s1, finds all other strings (in the list) s2 such that s1 is a substring of s2.
## Input
- A list of strings passed in through stdin.
## Output
- For each string s1, a list of all other strings which s1 is a substring of (sent to stdout).
## Space/Time Complexity
- Time complexity: O(N^2)
- Space complexity: O(N)

## Edge Case
- Input: ""
- Output: ""

## Test Case 1
- Input: ab, abdicate, ab, sabotage, age
- Output:
  - ab: abdicate, ab, sabotage
  - abdicate: 
  - ab: abdicate, ab, sabotage
  - sabotage: 
  - age: sabotage

## Test Case 2
- Input: cat, sat, bat
- Output:
  - cat: 
  - sat:
  - bat:
