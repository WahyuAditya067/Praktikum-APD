print("Pilih yang mau anda hitung")
print("1. Keliling segiempat")
print("2. Keliling segitiga")
print("3. Keliling lingkaran")
print("4. Luas segiempat")
print("5. Luas segitiga")
print("6. Luas lingkaran")
menu = int(input("Pilih menu : "))

if menu == 1:
    panjang = float(input("Masukkan panjang : "))
    lebar = float(input("Masukkan lebar : "))
    keliling = 2 * panjang + lebar * 2
    print(f"Keliling segiempat = {keliling}")

elif menu == 2:
    sisia = float(input("Masukkan panjang sisi A : "))
    sisib = float(input("Masukkan panjang sisi B : "))
    sisic = float(input("Masukkan panjang sisi C : "))
    keliling = sisia + sisib + sisic
    print(f"Keliling segitiga = {keliling}")

elif menu == 3:
    jari = float(input("Masukkan jari-jari : "))
    keliling = 3.14 * jari * 2
    print(f"Keliling lingkaran = {keliling}")

elif menu == 4:
    panjang = float(input("Masukkan panjang : "))
    lebar = float(input("Masukkan lebar : "))
    luas = panjang * lebar
    print(f"Luas segiempat = {luas}")

elif menu == 5:
    alas = float(input("Masukkan panjang alas : "))
    tinggi = float(input("Masukkan tinggi : "))
    luas = 0.5 * alas * tinggi
    print(f"Luas segitiga = {luas}")

elif menu == 6:
    jari = float(input("Masukkan jari-jari : "))
    luas = 3.14 * jari * jari
    print(f"Luas lingkaran = {luas}")

else:
    print("Keluar dari aplikasi")

