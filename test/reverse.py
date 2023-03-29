word = "abcdefghijk"
new_word = ""

#type1
for str in word:
    print(str)
    new_word = str+new_word

print(new_word)


new_word = ",".join(reversed(word))

print(new_word)


new_word = word[len(word):0:1]
print("1: "+new_word)
new_word = word[0:len(word):1]
print("2: "+new_word)
new_word = word[len(word):0:-1]
print("3: "+new_word)