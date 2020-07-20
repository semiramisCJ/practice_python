"""This code uses binary search to find
the square root of an integer defined by the user"""
# Variable initialization
target = int(input('Please enter an integer '))
epsilon = 0.1  # The error tolerance
result = 0.0
lower_bound = 0.0
upper_bound = target
result = (upper_bound + lower_bound) / 2

while(abs(result**2 - target) >= epsilon and result < target):
    if result**2 < target:
       lower_bound = result
    else:
        upper_bound = result
    result = (upper_bound + lower_bound) / 2
    print(f'Upper bound is: {upper_bound}, Lower bound is: {lower_bound}, Result is: {result}')


if(abs(result**2 - target) >= epsilon):
    print(f'Root not found')
else:
    print(f'The squared root of {target} is {result}')