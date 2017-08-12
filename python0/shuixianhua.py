#!/usr/bin/python
for i in range(10,1000):

    sum=0
    temp=i
    while temp:
        sum=sum+(temp%10)**3
        temp//=10
    if sum==i:
            print(i)
