# extra_ops.py
import math

def power(a, b):
    return a ** b

def factorial(n):
    if n < 0:
        return "Error: Factorial of negative number not allowed"
    return math.factorial(n)

def square(a):
    return a ** 2

def cube(a):
    return a ** 3
