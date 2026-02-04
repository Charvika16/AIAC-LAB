'''
Docstring for Lab-4.promptchaining
Generate a list of 5 consecutive numbers from 52401 to 52450
using the list generated above write a python function that finds and returns ending digits of 3, 5, 7
write a python statement that calls the function using above list and print last digit of 3,5,7
'''
# Generate a list of 5 consecutive numbers from 52401 to 52450
consecutive_numbers = list(range(52401, 52451))  # Create a list
# Function to find and return numbers ending with digits 3, 5, or 7
def find_ending_digits(numbers):
    """
    This function takes a list of numbers and returns a list of numbers
    that end with the digits 3, 5, or 7.
    """
    result = []  # Initialize an empty list to store results
    for number in numbers:  # Iterate through each number in the input list
        if str(number).endswith(('3', '5', '7')):  # Check if the number ends with 3, 5, or 7
            result.append(number)  # If it does, add it to the result list
    return result  # Return the list of numbers ending with 3, 5, or 7
# Call the function with the generated list and print the result
ending_digits = find_ending_digits(consecutive_numbers)  # Call the function
print("Numbers ending with 3, 5, or 7:", ending_digits) 