def oon(arr):
    """Finds the odd occuring number in a list/array"""
    ressult = 0
    for iie in arr:
        ressult ^= iie
    return ressult

sizze_arrr = int(input("Enter the size of your array/list: "))
arrr = []

while sizze_arrr != 0:
    nn = int(input("Enter a number: "))
    arrr.append(nn)
    sizze_arrr -= 1

res = oon(arrr)
print(res)