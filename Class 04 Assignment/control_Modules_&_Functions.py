import random
import math

# Arithmetic Calculator
def calculator(a, b, operation):
    if operation == "add":
        return a + b
    elif operation == "sub":
        return a - b
    elif operation == "mul":
        return a * b
    elif operation == "div":
        return a / b if b != 0 else "Cannot divide by zero"
    else:
        return "Invalid operation"

# String Reversal and Capitalization
def format_string(s):
    return s[::-1].capitalize()

# List of Even Numbers using Built-in Module
def generate_even_numbers(n):
    return [i for i in range(n+1) if i % 2 == 0]

# Test Function Outputs
print("Calculator: 12 + 5 =", calculator(12, 5, "add"))
print("Formatted String:", format_string("python"))
print("Even Numbers till 10:", generate_even_numbers(10))
