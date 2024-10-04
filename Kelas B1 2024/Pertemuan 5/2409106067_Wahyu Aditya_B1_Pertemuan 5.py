#kedua caranya sama aja
data = [1, 2, 3, 4, 5]
data_2 = list((1, 2, 3, 4, 5))

print(type(data))
print((data_2))

data_3 = [1, 2, 3, 4, True, [2, 3], "tes"]
print(data_3)

print(data_3[6])
#kalo data minus startnya dari paling belakang
print(data_3[-1])

data_4 = ["Apel", "Durian", "Jeruk"]
#kalo mau nambahin list di paling akhir
data_4.append("semangka")
print(data_4)

#kalo mau nambahin list sesuai posisi
data_4.insert(0, "rambutan")
print(data_4)

#kalo mau nambahin 2 data sekaligus
data_4.extend(["rambutan, semangka"])

#ngubah data
data_5 = ["Apel", "Durian", "Jeruk"]
data_5[0] = "Anggur" 
print(data_5)

#hapus data 1 (nilai dihapus dari memori)
del data_5[1]

#hapus data 2 (nilai masih ada tapi ga ditampilin)
data.pop(2)
nilai_hapus = data.pop(0)
print(nilai_hapus)

#kalo mau munculin data berulang
print(data_5*3)

data_mahasiswa = [
    ["060", "tes"],
    ["062", "tes2"]
]

print(data_mahasiswa[0][1])

data_mahasiswa_2 = [
    ["060", "tes"],
    ["062", "tes2"]
]

#print(data_mahasiswa[0][2][0])

buah = ["Apel", "Durian", "Jeruk"]

for data in buah:
    print(data)

buah = ["Apel", "Durian", "Jeruk"]

index = 1
for data in buah:
    print(f"data ke {index}")
    print(data)
    index = index + 1

for index, item in enumerate(buah):
    print(f"data ke {index + 1}")
    print(item)

tes_buah = ["Apel", "Durian", "Jeruk"]
buah1, buah2, buah3 = tes_buah
print(buah1)
print(buah2)
print(buah3)

import os
os.system("cls || clear")

data_mahasiswa_3 = ["ifnu", "Adi", "ucup", "michael"]
dataganti = int(input("data yang mau diganti : "))
data_mahasiswa_3[dataganti] = input("Masukkan nama pengganti :")
print(data_mahasiswa_3)

ifnu, Adi, ucup, michael = data_mahasiswa_3
datacari = int(input("data yang mau dicari : "))
print(data_mahasiswa_3[datacari])