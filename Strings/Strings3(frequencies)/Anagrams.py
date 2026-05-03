def is_anathar_grams(str1, str2):
    s1 = str1.replace(" ", "").lower()
    s2 = str2.replace(" ", "").lower()
    return sorted(s1), sorted(s2), sorted(s1) == sorted(s2)

str0 = input("String 1:\n")
str1 = input("String 2:\n")

print(is_anathar_grams(str0, str1))