'''
 read the number from user
check it is divisible by 2 or not
if yes display it as even
otherwise display it as odd
validate input to ensure it is an integer
well commented code
'''
#Read imput from user and validate it check it is even or odd
number_input = input("Enter a number: ")  # Prompt the user to enter a number
try:
    number = int(number_input)  # Try to convert the input to an integer
    # Check if the number is divisible by 2
    if number % 2 == 0:
        print(f"{number} is Even")  # If divisible, print that it is even
    else:
        print(f"{number} is Odd")  # If not divisible, print that it is odd