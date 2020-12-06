p=float(input("Enter the amount borrowed:"))
r=float(input("Enter the interest rate:"))
n=float(input("Enter the number of monthly payments:"))
r=r/100/12
print("The amount to be paid each month is:",(r*p)/(1-pow((1+r),-n)))