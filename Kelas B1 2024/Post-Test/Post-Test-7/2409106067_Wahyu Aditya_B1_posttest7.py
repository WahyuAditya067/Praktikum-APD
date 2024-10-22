import os
from fungsi import menuadmin, dataawal, datatambah, dataupdate, hapusdata, clear

clear ()

sistem = "Cek Pajak Kendaraan     "
maks = 3

users = [["admin", "admin1234", "admin"]]

print("=" * 30)
print(f"     {sistem}           ")
print("        Silahkan Login        ")
print("Register Jika Belum Punya Akun")

percobaan = 0

while True:
    print("1. Register")
    print("2. Login")
    print("3. Keluar")
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        username = input("Buat Username: ")
        password = input("Masukkan Password: ")
        role = input("Masukkan role (admin/user): ")
        
        if role == "admin" or role == "user":
            users.append([username, password, role])
            clear()
            print(f"Pengguna {username} Berhasil Registrasi")
        else:
            print("Role tidak valid. Harus admin atau user")

    elif pilihan == "2":
        username = input("Username: ")
        password = input("Password: ")
        user = None
        
        for i in users:
            if i[0] == username and i[1] == password:
                user = i
                break
        
        if user is None:
            percobaan += 1
            if percobaan >= maks:
                print("Login Gagal, Terlalu Banyak Percobaan")
                break
            print("Login gagal, username atau password salah")
        else:
            clear()
            percobaan = 0
            print(f"Selamat datang, {username}!")
            while True:
                if user[2] == "admin":
                    menuadmin()
                    pilihan_admin = input("Pilih menu: ")

                    clear()
                    if pilihan_admin == "1":
                        dataawal()

                    elif pilihan_admin == "2":
                        plat = datatambah()
                        clear()
                        print(f"Data {plat} berhasil ditambahkan")
                        
                    elif pilihan_admin == "3":
                        dataawal()
                        dataupdate('plat_baru', 'pajak_baru', 'status_baru')

                    elif pilihan_admin == "4":
                        dataawal()
                        datahapus = hapusdata()
                        clear()
                        print(f"Data {datahapus} berhasil dihapus")

                    elif pilihan_admin == "5":
                        clear()
                        break

                    else:
                        print("Pilihan tidak valid")

                else:
                    print("---- User ----")
                    print("1. Tampilkan Data")
                    print("2. logout")
                    pilihan_user = input("Pilih menu: ")

                    if pilihan_user == "1":
                        os.system("cls")
                        dataawal()

                    elif pilihan_user == "2":
                        clear()
                        break

                    else:
                        print("Pilihan tidak valid")
                    
    elif pilihan == "3":
        print("Terima kasih telah Menggunakan Aplikasi Ini")
        break

    else:
        print("Pilihan tidak valid. Silakan coba lagi")