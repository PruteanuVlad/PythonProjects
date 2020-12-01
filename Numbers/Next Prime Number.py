def prime(n):
    if n==2:
        return 1
    if n%2==0:
        return 0
    for i in range(3,n-1,2):
        if n%i==0:
            return 0
    return 1
