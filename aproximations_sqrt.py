"""This code uses successive approximations to find
the square root of an integer defined by the user"""
# Variable initialization
target = int(input('Please enter an integer '))
epsilon = 0.1  # The error tolerance
step = 0.1**2  # Step size can be smaller to gain accuracy
result = 0.0

while(abs(result**2 - target) >= epsilon and result <= target):
    result += step

if(abs(result**2 - target) >= epsilon):
    print(f'I could not find the anwser')
else:
    print(f'The squared root of {target} is {result}')