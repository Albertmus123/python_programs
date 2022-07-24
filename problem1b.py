# Python program to find Minimum
list1 = []
num = int(input("Enter Element number: "))
for i in range(1, num + 1):
	element = int(input("Enter elements %d: "%i))
	list1.append(element)
min=list1[0]
for x in list1:
        if x < min :
             min = x
     
print("Minimum Element is:", min)