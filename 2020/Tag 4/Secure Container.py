counter = 0
for i in range(123257, 647016):
    j = str(i)
    if j[0] <= j[1] <= j[2] <= j[3] <= j[4] <= j[5] and (j[0] == j[1] or j[1] == j[2] or j[2] == j[3] or j[3] == j[4] or j[4] == j[5]):
        counter += 1
print(counter)


def check(n):
    return list(n) == sorted(n) and 2 in map(n.count, n)

print(sum(check(str(n)) for n in range(123257, 647016)))