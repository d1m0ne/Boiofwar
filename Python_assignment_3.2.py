print("Please enter three numbers!")

N1 = input()

N2 = input()

N3 = input()

if (int(N1) > int(N2) and int(N2) > int(N3)) or (int(N2) > int(N1) and int(N2) < int(N3)):
    print(N2)
elif (int(N1) < int(N2) and int(N1) > int(N3)) or (int(N1) > int(N2) and int(N1) < int(N3)): 
    print(N1)
else:
    print(N3)