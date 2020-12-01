n1=0
n2=1
n3=0
i=1
mode=0
mode=int(input("Enter 1 to genertate the Fibonacii sequence to the Nth term. Enter 2 to generate the Fibonacii sequence to N."))
n=int(input("Enter the number N."))
if mode==1:
    if n==0:
        print("0")
        quit()
    if n==1:
        print("0 1",end=" ")
        quit()
    print("0 1",end=" ")
    while i<=n:
        n3=n1+n2
        n1=n2
        n2=n3
        print(n3,end=" ")
        i=i+1
if mode==2:
    if n==0:
        print("0")
        quit()
    if n==1:
        print("0 1 1",end=" ")
        quit()
    print("0 1",end=" ")
    while n3<=n:
        n3=n1+n2
        n1=n2
        n2=n3
        if n3<=n:
            print(n3,end=" ")
quit()  