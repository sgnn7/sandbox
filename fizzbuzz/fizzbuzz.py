#!/usr/bin/env python3

# Fun solution - list comprehension
# print('\n'.join(["FizzBuzz" if not (num % 3 or num % 5)
#                  else "Buzz" if not num % 5
#                       else "Fizz" if not num % 3
#                            else str(num) for num in range(1,101)]))

# Fun solution2 - zipping
list_range = range (1,101)
mod_3_list = ['' if num % 3 else "Fizz" for num in list_range]
mod_5_list = ['' if num % 5 else "Buzz" for num in list_range]
numbers = [str(num) if num % 3 and num % 5 else '' for num in list_range]

for items in zip(numbers, mod_3_list, mod_5_list):
    print('%s%s%s' % items)

# Maintainable solution
# for index in range (1, 101):
#     if index % 3 == 0 and index % 5 == 0:
#         print("FizzBuzz")
#     elif index % 3 == 0:
#         print("Fizz")
#     elif index % 5 == 0:
#         print("Buzz")
#     else:
#         print(index)
