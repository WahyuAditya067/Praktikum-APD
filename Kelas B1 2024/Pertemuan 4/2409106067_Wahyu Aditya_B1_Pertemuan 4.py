batas = 20
for i in range(batas):
    print(f"Perulamgan ke-{i}")

batas = 20
for i in range(1, batas, 2):
    print(f"Perulamgan ke-{i}")

buah = ["Apel", "Mangga", "Anggur"]
for i in buah:
    print(i)

buah_banyak = ["Apel", "Mangga", "Anggur", "Semangka"]
for buah in buah_banyak:
    if buah == "anggur":
        print("buah anggur ketemu")
        break
    else:
        print(buah)

for baris in range(1,4):
    for kolom in range(1,4):
        print(kolom, "kolom", end=" ")
    print()

for baris in range(1,4):
    print("Baris ke", baris)
    for kolom in range(1,4):
        print(kolom, "kolom", end=" ")
    print()
    print()

lagi = "Yes"
while lagi == "Yes":
    print("Mabar")
    lagi = input("Mabar lagi gak?")
print("Selesai mabar")

lagi = "Yes"
ulang = 0
while lagi == "Yes":
    ulang += 1
    print("Mabar")
    lagi = input("Mabar lagi gak?")
print("Selesai mabar")
print(f"Perulangan terjadi sebanyak {ulang} kali")

for i in range(1,10):
    if i == 4:
        break
    else:
        print(f"perulangan ke {i}")

while True:
    ulang = input("Mabar lagi")
    if ulang == "ga":
        break
    print("Mabar lagi")

for i in range(1, 10):
    if i == 4:
        continue
    print(f"perulangan ke {i}")

#for i in range(1,20):
    #if i % 2 == 0:

for i in range(5):
    for j in range(5):
        print("*" , end="")
    print()

print("segitiga siku")
for i in range(1, 5):
    print("*" + 1)

print("segitika sama kaki")
for i in range(batas):
    print(" " * (batas - i))


kesempatan = 3

while kesempatan >0:
    username = input("Masukkan username :")
    password = input("Masukkan password :")

    if username == "admin" and password == "admin1234":
        print("Berhasil login")
        break
    else:
        print("username atau password salah")
        print("kesempatan login tersisa {kesempatan}")
        kesempatan -= 1

print("Program utama")