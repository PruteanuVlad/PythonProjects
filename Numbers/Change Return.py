import math
c=float(input("Enter the cost, up to 2 decimals:"))
p=float(input("Enter the amount paid, up to 2 decimals:"))
d=p-c
print("The change is:")
print(math.floor(d/200),"200 euro banknote(s)")
d=d-math.floor(d/200)*200
print(math.floor(d/100),"100 euro banknote(s)")
d=d-math.floor(d/100)*100
print(math.floor(d/50),"50 euro banknote(s)")
d=d-math.floor(d/50)*50
print(math.floor(d/20),"20 euro banknote(s)")
d=d-math.floor(d/20)*20
print(math.floor(d/10),"10 euro banknote(s)")
d=d-math.floor(d/10)*10
print(math.floor(d/5),"5 euro banknote(s)")
d=d-math.floor(d/5)*5
print(math.floor(d/2),"2 euro coin(s)")
d=d-math.floor(d/2)*2
print(math.floor(d/1),"1 euro coin(s)")
d=d-math.floor(d/1)*1
d=d*100
print(math.floor(d/50),"50 eurocents coin(s)")
d=d-math.floor(d/50)*50
print(math.floor(d/20),"20 eurocents coin(s)")
d=d-math.floor(d/20)*20
print(math.floor(d/10),"10 eurocents coin(s)")
d=d-math.floor(d/10)*10
print(math.floor(d/5),"5 eurocents coin(s)")
d=d-math.floor(d/5)*5
print(math.floor(d/2),"2 eurocents coin(s)")
d=d-math.floor(d/2)*2
print(math.floor(d/1),"1 eurocents coin(s)")