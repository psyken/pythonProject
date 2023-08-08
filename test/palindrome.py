word = "abba"
reversed_word = word[::-1]
#print(reversed_word)
if(reversed_word==word):
    print(True)
else:
    print(False)



str = "amail"
str = "".join(reversed(str))
print(str)