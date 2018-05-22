import math

def is_prime(number):
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for current in range(3, int(math.sqrt(number) + 1), 2):
            if number % current == 0:
                return False
        return True
    return False

# Not a generator
# def get_primes(input_list):
#     result_list = list()
#     for element in input_list:
#         if is_prime(element):
#             result_list.append()
#     return result_list

# More Pythonic
# def get_primes(input_list):
#     return (element for element in input_list if is_prime(element))

# Generator
def get_primes(number):
    # Using while makes sure we never reach the end of the function
    while True:
        if is_prime(number):
            yield number
        number += 1

"""
Flow:
    When the for loop requests the first value from get_primes...
        1. Enter while loop
        2. The if condition holds (3 is prime)
        3. We yield the value 3 and control to solve_number_10
    Then, back in solve_number_10:
        1. The value 3 is passed back to the for loop
        2. The for loop assigns next_prime to this value
        3. next_prime is added to the total
        4. The for loop requests the next element from get_primes
"""
def solve_number_10():
    total = 2
    for next_prime in get_primes(3):
        if next_prime < 2000000:
            total += next_prime
        else:
            print(total)
            return
