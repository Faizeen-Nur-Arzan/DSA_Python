def does_it_EXIST(s1, s2):
    yup = s1.split()
    if s2 in yup:
        return True
    else:
        return "iT dOEsN'T eXiSt"

s1 = input("Steering\n:")
s2 = input("Werd\n:")
print(does_it_EXIST(s1, s2))