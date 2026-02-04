#write a python program that display all disarium nymbers within range 100 to 300
def is_disarium(num):
    str_num = str(num)
    length = len(str_num)
    sum_of_powers = sum(int(digit) ** (index + 1) for index, digit in enumerate(str_num))
    return sum_of_powers == num
disarium_numbers = []
for number in range(100, 301):
    if is_disarium(number):
        disarium_numbers.append(number)
print("Disarium numbers between 100 and 300 are:", disarium_numbers)
