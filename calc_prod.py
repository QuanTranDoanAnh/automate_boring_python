import time, sys

def calc_prod():
    """
    Converting between int and str in bases other than 2 (binary), 4, 8 (octal), 
    16 (hexadecimal), or 32 such as base 10 (decimal) now raises a ValueError 
    if the number of digits in string form is above a limit to avoid potential 
    denial of service attacks due to the algorithmic complexity. This is a 
    mitigation for CVE-2020-10735. This limit can be configured or disabled by 
    environment variable, command line flag, or sys APIs. See the integer string 
    conversion length limitation documentation. The default limit is 4300 digits 
    in string form.
    """
    sys.set_int_max_str_digits(0)
    # Calculate the product of the first 100,000 numbers.
    product = 1
    for i in range(1, 100000):
        product = product * i
    return product

start_time = time.time()
prod = calc_prod()
end_time = time.time()
print('The result is %s digits long.' % (len(str(prod))))
print('Took %s seconds to calculate.' % (end_time - start_time))