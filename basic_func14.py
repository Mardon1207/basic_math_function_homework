from math import trunc
def main(a, b):
    '''find the floor division of a and b and return it.
    
    Args:
        a (int): a number
        b (int): a number
        
    Returns:
        int: the result.
    '''
    return trunc(a/b)
a=int(input())
b=int(input())
print(main(a,b))