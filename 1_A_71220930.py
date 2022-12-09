a= int(input("Masukan awal deret: "))
b= int(input("Masukan akhir deret: "))

jumlah = 0
for count in range(a,b):
    if count%6 != 0 and count%3 != 0 and count%2 == 1: 
        print(count, end=' ')
