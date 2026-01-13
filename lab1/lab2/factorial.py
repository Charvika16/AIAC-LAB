#write a python code to display factorial using Recursion  model
def factorial_recursive(n):
    if n<0:
        return "Factorial is not defined for negative numbers"
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)
number = int(input("Enter a number to check if it is factorial: "))
factorial_result = factorial_recursive(number)
print(f"The factorial of {number} is {factorial_result}")