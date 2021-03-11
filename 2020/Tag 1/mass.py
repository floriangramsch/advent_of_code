datei = open("Mass.txt")

summe = []
new = []
end = []
for line in datei:
    summe.append(int(line))

for i in summe:
    a = 0
    while i > 0:
        i = i//3 - 2
        if i > 0:
            new.append(i)
        else:
            end.append(sum(new))
            new = []

print(sum(end))
datei.close()