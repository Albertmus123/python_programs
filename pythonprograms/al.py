# def string_test(s):
#     uppercounter = 0
#     lowercounter = 0
#     for i in s:
#         if i.isupper():
#             uppercounter+=1
#         else:
#             lowercounter+=1
#     print(uppercounter)
#     print(lowercounter)

# word = input("Enter a word: ")
# print(string_test(word))

def string_test(word):
    ucounter=0
    lcounter=0
    for i in word:
        if i.isupper():
            ucounter+=1
        else:
            lcounter+=1
    print(ucounter)
    print(lcounter)            


word = input("Enter Your Word : ")
print(string_test(word))    