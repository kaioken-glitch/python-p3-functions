#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")

def greet(name):
    print(f"Hello, {name}!")

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")

def add(num1, num2):
    return num1 + num2

def halve(number):
    return number / 2


# def keyword used to identify the code as a function definition
# Function names should be descriptive and use snake_case
# Parameters are specified within parentheses after the function name
# The body of the function is indented and contains the code that runs when the function is called
# Indentation is crucial in Python to define the scope of the function
#insread of a closing curtly brace, Python uses indentation to define blocks of code
# Functions can take parameters, which are variables that allow you to pass data into the function
# Default parameter values can be specified in the function definition
# Functions can return values using the return statement, but in this case, they do not return anything


##Arguments can be passed to functions when they are called
# Functions can also be called without any arguments if they have default values

##Default Arguments allow functions to be called with fewer arguments than defined
# If a function does not return a value, it implicitly returns None
# Functions can be used to encapsulate reusable code, making it easier to maintain and understand

##Return values
# Functions can be called multiple times with different arguments
# The return statement is used to exit a function and optionally return a value
# Functions can be defined at the module level or within other functions
# Functions can be documented using docstrings, which are multi-line strings that describe the function's purpose and usage
# Python's built-in functions can be used alongside user-defined functions
# Functions can be nested, meaning you can define a function inside another function
# Functions can also accept variable-length arguments using *args and **kwargs