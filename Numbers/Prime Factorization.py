def prime(n):
    if n==2:
        return 1
    if n%2==0:
        return 0
    for i in range(3,n-1,2):
        if n%i==0:
            return 0
    return 1

n=int(input("Enter the number N:"))
print("The prime factors are:")
for i in range (2,n):
    if prime(i):
        if n%i==0:
            print(i,end=" ")
quit()