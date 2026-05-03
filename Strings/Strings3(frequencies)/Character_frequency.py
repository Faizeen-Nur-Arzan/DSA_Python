def char_freq(string):
    dictionary = {}
    for i in string:
        if i in dictionary:
            dictionary[i] += 1
        else:
            dictionary[i] = 1
    return dictionary

str0 = "Pneumonoultramicroscopicsilicovolcanoconiosis"
str1 = "Giraffe"
str2 = "AaaaaaaaaaaaaaaaaaaaAAAAAAaaaaaaaaaaaaaaaaabbbbbbbbbbBBBBBBBBbbbbbbbbbbbbbbbbbbbbcccccccccCCCCCCcccccccccccccccccccccdddddddddddddddddddddddddddddddddddddddddddddddddddeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee"

print(char_freq(str0))
print(char_freq(str1))
print(char_freq(str2))