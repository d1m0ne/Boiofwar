print("Please enter 5 numbers.")

Nlist = []

for i in range (0, 5):
    Input = int(input())
    Nlist.append(Input)

evencount = 0

for i in range(len(Nlist)):
    if Nlist[i] % 2 == 0:
        evencount += 1

print(evencount)