N = int(input("Masukkan nilai N : "))

print("Anak Ayam Turun " + str(N))

while(N>1):
    print("Anak Ayam Turun " + str(N) + "," + " Hilang Satu Tinggal " + str(N-1))
    N -= 1

print("Anak Ayam Turun 1, Hilang Satu Tinggal Induknya")    
