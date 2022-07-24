set=[]
def sumfind(limit):
  sum=0
  for i in range(1,limit+1):
    elements=int(input("Enter elements %d:"%i))
    set.append(elements)
    for x in set:
     sum=sum+x
  print(set)
  return sum

x = int(input("Enter limit:"))
print(sumfind(x))