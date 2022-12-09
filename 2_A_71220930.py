kalimat = input("Masukan nama : ")
x = len(kalimat)

for i in range(x):
    for col in range(i+1):
        print(kalimat[col],end=' ')
    print()
for i in range (x,0,-1):
    for col in range (0,i-1):
        print (kalimat[col],end=' ')
    print()
