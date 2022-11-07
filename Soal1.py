jumlah = int(input("Masukkan jumlah : "))

data = []
for i in range(jumlah):
    inputan = input("Masukkan kata : ")
    data.append(inputan)

z = 0
for i in data :
    print("Hasilnya adalah: ")
    for j in i :
        if z < len(i) - 1:
            if ord(i[z]) > ord(i[z+1]):
                hasil = ord(i[z]) - ord(i[z+1])
                print(i[z],"lebih dari",i[z+1],", selisih",hasil)
                z += 1
            elif ord(i[z]) < ord(i[z+1]):
                hasil = ord(i[z+1]) - ord(i[z])
                print(i[z],"kurang dari",i[z+1],", selisih",hasil)
                z += 1
            elif ord(i[z]) == ord(i[z+1]):
                hasil  = 0
                print(i[z],"sama dengan",i[z+1],", selisih",hasil)
                z += 1
        elif z == len(i) - 1:
            z = 0
    print("")