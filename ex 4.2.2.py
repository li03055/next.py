def parse_ranges(ranges_string):
    num1_generator = (range.split('-') for range in ranges_string.split(','))   # get the numbers written in the string
    num2_generator = (num for start, stop in num1_generator for num in range(int(start), int(stop) + 1))    # add the numbers in between
    return num2_generator

print(list(parse_ranges("1-2,4-4,8-10")))
print(list(parse_ranges("0-0,4-8,20-21,43-45")))