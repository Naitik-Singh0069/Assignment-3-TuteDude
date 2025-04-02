'''
1.   Asks the user for a number as input.
2.   Uses the math module to calculate the:
o   Square root of the number
o   Natural logarithm (log base e) of the number
o   Sine of the number (in radians)
3.   Displays the calculated results.
'''
import math
n = int(input('Enter a number: '))
sqrt = math.sqrt(n)
log = math.log(n)
sin = math.sin(n)
print(f'Square root of {n}: {sqrt}')
print(f'Natural logarithm of {n}: {log}')
print(f'Sine of {n}: {sin} radians')