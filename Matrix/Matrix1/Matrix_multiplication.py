x = [[8, 2], [4, 1]]
y = [[3, 8], [9, 5]]
a = [[0, 0], [0, 0]]

for i in range(len(x)):
    for j in range(len(y[0])):
        for k in range(len(y)):
            a[i][j] += x[i][k] * y[k][j]

print(f"Matrix X = {x}\nMatrix Y = {y}\nMultiplication = {a}")