# Simple Python Calculator

## Project Description
A command-line calculator application that performs basic arithmetic operations using Python functions. The calculator takes user input for numbers and operations, then returns the calculated result. This project demonstrates the understanding of functions, variables, and basic user input/output in Python.

## Features
- Addition (+)
- Subtraction (-)
- Multiplication (*)
- Division (/)
- Power (**)
- Remainder/Modulus (%)

## Requirements
- Python 3.x
- No additional libraries required

## File Structure
```
calculator/
│
├── calculator.py    # Main program file
└── README.md       # Documentation
```

## Function Specifications

The program should implement the following functions:

1. `get_numbers()`: 
   - Gets two numbers from user input
   - Validates that the input is numeric
   - Returns both numbers as floats

2. `get_operation()`:
   - Gets the desired operation from user input
   - Validates that it's a supported operation
   - Returns the operation symbol

3. `calculate(num1, num2, operation)`:
   - Takes two numbers and an operation as parameters
   - Performs the requested calculation
   - Returns the result
   - Handles division by zero scenarios

4. `main()`:
   - Controls the program flow
   - Calls other functions as needed
   - Handles program repetition
   - Displays results

## Usage Example
```python
Enter first number: 10
Enter operation (+, -, *, /, **, %): *
Enter second number: 5
Result: 50

Would you like to calculate again? (yes/no): no
```

## Error Handling
The program should handle:
- Invalid number inputs
- Invalid operation inputs
- Division by zero
- Other potential runtime errors

## Learning Objectives
Through this project, you will learn:
- Function declaration and calling
- Variable scope
- User input handling
- Basic arithmetic operations
- Type conversion
- Basic error handling
- Program flow control

## Bonus Challenges
1. Add support for more operations (square root, factorial)
2. Allow for calculations with more than two numbers
3. Add memory function to store previous results
4. Implement a history feature to show past calculations

## Testing
Test your calculator with various scenarios:
- Positive numbers
- Negative numbers
- Zero
- Decimal numbers
- Invalid inputs

## Tips for Implementation
1. Start with basic functionality and add features incrementally
2. Test each function as you write it
3. Consider edge cases in your error handling
4. Use clear variable names that indicate their purpose
5. Add comments to explain complex logic

## Expected Output Example
```
Welcome to Python Calculator!
=========================

Enter first number: 15
Enter operation (+, -, *, /, **, %): +
Enter second number: 5
Result: 20

Would you like to calculate again? (yes/no): yes

Enter first number: 
```

Remember to document your code and handle user input gracefully to create a robust and user-friendly calculator application.