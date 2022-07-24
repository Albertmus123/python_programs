def string_test(s):
    uppercounter = 0
    lowercounter = 0
    for i in s:
        if i.isupper():
            uppercounter+=1
        else:
            lowercounter+=1
    print(uppercounter)
    print(lowercounter)

word = input("Enter a word: ")
print(string_test(word))
