'''
1.   Defines a function named factorial that takes a number as an argument and calculates its factorial using a loop or recursion.
2.   Returns the calculated factorial.
3.   Calls the function with a sample number and prints the output.
'''

def fn(a):
    if a <=1:
        return 1
    else:
        return a * fn(a-1)     
print(fn(int(input('Enter a number: '))))