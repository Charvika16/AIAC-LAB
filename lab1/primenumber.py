# write a python code to define a function to check if a number is prime or not generate optimal code. and also count  how many iteration it takes

# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True
#     number = int(input("Enter a number to check if it is prime: "))
#     if is_prime(number):
#         print(f"{number} is a prime number.")
#     else:
#         print(f"{number} is not a prime number.")
# # Example usage
# number = int(input("Enter a number to check if it is prime: "))
# if is_prime(number):
#     print(f"{number} is a prime number.")   
# else:
#     print(f"{number} is not a prime number.")

# Optimized code
# def is_prime(n):
#     if n <= 1:
#         return False
#     if n <= 3:
#         return True
#     if n % 2 == 0 or n % 3 == 0:
#         return False
#     i = 5
#     while i * i <= n:
#         if n % i == 0 or n % (i + 2) == 0:
#             return False
#         i += 6
#     return True
# # Example usage
# number = int(input("Enter a number to check if it is prime: "))
# if is_prime(number):
#     print(f"{number} is a prime number.")
# else:
#     print(f"{number} is not a prime number.")

# Further optimized code with iteration count
def is_prime(n):
    iteration_count = 0
    if n <= 1:
        return False, iteration_count
    if n <= 3:
        return True, iteration_count
    if n % 2 == 0 or n % 3 == 0:
        iteration_count += 1
        return False, iteration_count
    i = 5
    while i * i <= n:
        iteration_count += 1
        if n % i == 0 or n % (i + 2) == 0:
            return False, iteration_count
        i += 6
    return True, iteration_count
# Example usage
number = int(input("Enter a number to check if it is prime: "))
is_prime_result, iterations = is_prime(number)
print (f"Number of iterations: {iterations}")
if is_prime_result:
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")
    