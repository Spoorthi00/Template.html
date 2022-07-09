import math
num=int(input("Enter a number"))
m=num
sum=0
while num>0:

    rem=num%10
    fact=math.factorial(rem)
    sum=sum+fact
    num=num//10
if sum==m:
    print('Number is Peterson number')
else:
    print('Number is not a Peterson number')