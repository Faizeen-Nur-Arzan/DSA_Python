#Circuit

a = int(input("Enter a number for A: "))
b = int(input("Enter a number for B: "))
c = int(input("Enter a number for C: "))

q = (a & b) | ((b | c) & (b & c))

print(f"The circuit in python bitwise code is:\nQ = (A & B) | ((B | C) & (B & C)\nA = {a}\nB = {b}\nC = {c}\nSo, Q = {q}.")