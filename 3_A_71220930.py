a = int(input("Masukan Pembatas : "))
b = int(input("Masukan Angka yang dilarang : "))
for i in range(a):
    if i == b:
        continue
    print(i, ' ', end='')

