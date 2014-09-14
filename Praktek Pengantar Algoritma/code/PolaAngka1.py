N = int(input("Masukkan nilai N : "))

pembilang = 1
penyebut = 1
hasil = pembilang / penyebut
total = hasil
print(str(pembilang) + "/" + str(penyebut) + " = " +  ("%.2f" % hasil))

perulangan = 1
while(perulangan < N):
    penyebut += 2
    hasil = pembilang / penyebut
    total += hasil
    print(str(pembilang) + "/" + str(penyebut) + " = " + ("%.2f" % hasil))
    perulangan += 1

print("%.2f" % total)
    
