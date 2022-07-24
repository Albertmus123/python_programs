#Write a program which accepts a sequence of comma separated 4 digit binary 
#The numbers that are divisible by 5 are to be printed in a comma separated sequence

print("Enter a List of number separated by , here: ")
value = []
items=[x for x in input().split(',')]
for p in items:
    intp = int(p, 2)
    if not intp%5:
        value.append(p)

print(','.join(value))