x = [1, 2, 3, 4, 5, 1, 3, 52, 2, 3, 2]
y = {}
for item in x:
    y[item] = x.count(item)
y = sorted(y, key=y.get)
