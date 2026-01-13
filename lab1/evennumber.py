# 1.write a python code to check if a number is even or not
#for i in range(1, 501):
 #   if i % 2 == 0:
  #      print(i,end= ",")

  # 2.write a python code to display even numbers from 1 to 500 use minimum lines
#print([num for num in range(1, 501) if num % 2 == 0])
# 3.or
#for i in range(2, 501, 2): print (i)
# 4. or
def display_even_numbers(start, end):
    even_numbers = [num for num in range(start, end + 1) if num % 2 == 0]
    return even_numbers
if __name__ == "__main__":
    start_range = 1
    end_range = 500
    even_numbers= display_even_numbers(start_range, end_range)
    print("Even numbers from", start_range, "to", end_range, "are:")
    print(even_numbers)