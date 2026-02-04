#generate a function that displays all Automorphic numbers between 1 and 1000 using a for loop.
def is_automorphic(num):
    square = num * num
    return str(square).endswith(str(num))
def display_automorphic_numbers():
    automorphic_numbers = []
    for i in range(1, 1001):
        if is_automorphic(i):
            automorphic_numbers.append(i)
    return automorphic_numbers
# Call the function and print the result
automorphic_numbers = display_automorphic_numbers()
print("Automorphic numbers between 1 and 1000 are:", automorphic_numbers)
    