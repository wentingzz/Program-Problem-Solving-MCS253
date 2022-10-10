# Program to Process and Print Parenthesized Text by Nesting Levels

## Overview

This program reads a string of parenthesized text and, if the parentheses are valid, prints the text at each nesting level preceded by spaces indicating the level of nesting. If the parentheses are invalid, it prints an error message.

## Input

A string of parenthesized text from stdin.

## Output

- If the parentheses are valid, the program prints the text of each nesting level preceded with two spaces for each level of nesting.
- If the parentheses are invalid, it prints an error message.

## Algorithm

1. **Initialize Data Structures**:
   - An unordered map/hash table for open parentheses: `open_paren_map = {'(': ')', '[': ']', '{': '}'}`
   - An ordered map for stack size to string: `level_map = {}` (ordered dictionary)
   - A vector (stack) for open parentheses: `stack = []`

2. **Iterate through the Input String**:
   - For each character in the input string:
     - If the character is an open parenthesis (exists in `open_paren_map`), append it to the `stack`.
     - If the character is a closing parenthesis, check if it matches the top of the `stack`:
       - If it matches, remove the top element from the `stack`.
       - If it doesn't match, print an error message: "Mismatched parentheses!" and exit.
     - If the character is neither an open nor closing parenthesis, append it to the `level_map` with the key being the current `stack` size.

3. **Validate the Stack**:
   - After iterating through the input, if the `stack` is not empty, print an error message: "Mismatched parentheses!" and exit.

4. **Print the Results**:
   - Iterate through the `level_map` and print the text at each nesting level preceded by spaces indicating the level of nesting.

## Test Cases

- TC1: (does{[[well!]]}work)this 
- TC2: (doesn’t{[[work!]})this 
- TC3: Hell(is{all[are]}empty{the}(devils((here)))and)
- TC4: {([])[]} 
- TC5:  

## Sample Run
```commandline
python printNesting.py (does{[[well!]]}work)this 
```
