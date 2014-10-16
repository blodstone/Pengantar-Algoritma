n = 2
m = 8
kali = 1
jumlah = 0

for i in range(n):
    hasil = 1
    for j in range(kali * m, 0, -1):
        hasil *= j
    kali += 1
    jumlah += hasil

rata = jumlah / n
print(rata)
