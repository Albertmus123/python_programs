def sumlimit(limit):
 set=[]
 sum=0;
 for i in range(1,limit+1):
    if i%3==0 or i%5==0:
        set.append(i)
        sum=sum+i

 print(set)
 return sum
x=int(input("Enter limits:"))
print(sumlimit(x))




