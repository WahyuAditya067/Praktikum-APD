import os
os.system('cls')

print ("Silahkan Login Terlebih dahulu")

id = "wahyu"
pw = 67
salah = 0

while salah < 3 :
    username = (input("Masukkan Username anda = "))
    password = int(input("Masukkan password anda = "))

    if username == id and password == pw :
        print ("Login Anda Berhasil")
        break
    else :
        salah += 1
        print ("Anda salah memasukkan username atau password")
if salah < 3 :
        while True :
            print("Pilih yang mau anda hitung")
            print("1. Keliling segiempat")
            print("2. Keliling segitiga")
            print("3. Keliling lingkaran")
            print("4. Luas segiempat")
            print("5. Luas segitiga")
            print("6. Luas lingkaran")
            menu = int(input("Pilih menu : "))

            if menu == 1:
                print("Menu 1 (Keliling Segiempat)")
                panjang = float(input("Masukkan panjang : "))
                lebar = float(input("Masukkan lebar : "))
                keliling = 2 * panjang + lebar * 2
                print(f"Keliling segiempat = {keliling}")

            elif menu == 2:
                print("Menu 2 (Keliling Segitiga)")
                sisia = float(input("Masukkan panjang sisi A : "))
                sisib = float(input("Masukkan panjang sisi B : "))
                sisic = float(input("Masukkan panjang sisi C : "))
                keliling = sisia + sisib + sisic
                print(f"Keliling segitiga = {keliling}")

            elif menu == 3:
                print("Menu 3 (Keliling Lingkaran)")
                jari = float(input("Masukkan jari-jari : "))
                keliling = 3.14 * jari * 2
                print(f"Keliling lingkaran = {keliling}")

            elif menu == 4:
                print("Menu 4 (Luas Segiempat)")
                panjang = float(input("Masukkan panjang : "))
                lebar = float(input("Masukkan lebar : "))
                luas = panjang * lebar
                print(f"Luas segiempat = {luas}")

            elif menu == 5:
                print("Menu 5 (Luas Segitiga)")
                alas = float(input("Masukkan panjang alas : "))
                tinggi = float(input("Masukkan tinggi : "))
                luas = 0.5 * alas * tinggi
                print(f"Luas segitiga = {luas}")

            elif menu == 6:
                print("Menu 6 (Luas Lingkaran)")
                jari = float(input("Masukkan jari-jari : "))
                luas = 3.14 * jari * jari
                print(f"Luas lingkaran = {luas}")

            else:
                print("Keluar dari aplikasi")
            
            print("Menu : 1. Ulangi program")
            print("       2. Keluar") 
            
            menu = int(input("Masukkan Pilihan Anda : "))
            if menu == 1:
                continue
            else:
                print("Terima Kasih Telah Menggunakan Program ini")
                break

if salah == 3 :
    print ("Kesempatan login anda habis")