def check_vowel(str):
    return_boolean = False
    vowel_tuple = ("a","e","i","o","u") #튜플 선언
    for i in str:
        for j in vowel_tuple:
            if(i.find(j)>-1): #존재한다면
                return_boolean = True

    return return_boolean


print(check_vowel("baiaba"))



def check_vowel2(string):
    vowels = "aeiou"
    for char in string:
        if char in vowels:
            return True
    return False

print(check_vowel2("bbbbb"))