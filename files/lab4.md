# Multiplication

`multiply.py` is a simple Python script that multiplies two numbers provided as command-line arguments and prints the result.

## Requirements

- Python 3.x

## Usage

To use this program, open your terminal or command prompt and run the script with two numerical arguments.

### Syntax

```bash
python multiply.py <num1> <num2>
```
### Example 
```bash
python multiply.py 5 10
```
This will output `50`
### Error Handling
- The script checks if exactly two arguments are provided.
- If the arguments are not numbers, it prints an error message and exits. 
- It handles cases where one or both numbers are 0. 
- It correctly handles negative numbers.