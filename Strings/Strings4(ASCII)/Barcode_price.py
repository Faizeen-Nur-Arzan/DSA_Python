def read_barcode(bc):
    result = 0
    for i in bc:
        result += ord(i)
    print(result)

useless_barcode = "GN\\@|L"
print("Price", end=" ")
read_barcode(useless_barcode)

useless_barcode = ""
print("Price", end=" ")
read_barcode(useless_barcode)