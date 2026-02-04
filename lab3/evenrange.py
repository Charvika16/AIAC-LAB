def even_numbers_within_range(start, end):
    for number in range(start, end + 1):#loop runs from start to end to end -1
        if number % 2 == 0:
            print(number, end=' ')
even_numbers_within_range(500,1000)
