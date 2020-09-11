Nlist = [3, 2, 8, 9, 17, 24]

evencount = 0

for i in range(len(Nlist)):
    if Nlist[i] % 2 == 0:
        evencount += 1

print(evencount)