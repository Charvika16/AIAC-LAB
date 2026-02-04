#display all perfect numbers within a range 1 to 1000
def is_perfect(num):
    sum_of_divisors = sum(i for i in range(1, num) if num % i == 0)
    return sum_of_divisors == num
perfect_numbers = []
for number in range(1, 1001):
    if is_perfect(number):
        perfect_numbers.append(number)
print("Perfect numbers between 1 and 1000 are:", perfect_numbers)
