'''
Digital root is the recursive sum of all the digits in a number.

Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing in this way until a single-digit number is produced. The input will be a non-negative integer.
16  -->  1 + 6 = 7
942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
'''
def digital_root(n):
    n = list(str(n))
    if len(n) > 1:
        n = [int(x) for x in n]
        a = sum(n)
        x = list(str(a))
        while len(x) > 1:
            n = [int(b) for b in x]
            a = sum(n)
            x = list(str(a))
            
        return(a)
    else:
        n = [int(x) for x in n]
        return sum(n)
