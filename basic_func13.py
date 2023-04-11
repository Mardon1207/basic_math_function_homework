def main(a):
    '''find the square root of a number and return it.
    
    Args:
        a (int): a number
        
    Returns:
        float: the absolute value.
    '''
    return pow(a,1/2)
a=int(input())
print(main(a))