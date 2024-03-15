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
