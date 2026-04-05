x = [[8, 2], [6, 4]]
y = [[1, 7], [5, 9]]
a = [[0, 0], [0, 0]]

for i in range(len(x)):
    for j in range(len(x[0])):
        a[i][j] = x[i][j] + y[i][j]

print(f"Matrix X = {x}\nMatrix Y = {y}\nAddition = {a}")