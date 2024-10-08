import os
os.system("cls")

users = [["admin", "admin1234", "admin"]]
data = [ ]

print("=" * 30)
print("     Cek Pajak Kendaraan      ")
print("        Silahkan Login        ")
print("Register Jika Belum Punya Akun")

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
            print("Login gagal, username atau password salah")
        else:
            os.system("cls")
            print(f"Selamat datang, {username}!")
            while True:
                if user[2] == "admin":
                    print("--- Menu Admin ---")
                    print("1. Tampilkan Data")
                    print("2. Tambah Data")
                    print("3. Update Data")
                    print("4. Hapus Data")
                    print("5. Logout")
                    pilihan_admin = input("Pilih menu: ")

                    os.system("cls")
                    if pilihan_admin == "1":
                        if len(data) == 0:
                            print("Data kosong")
                        else:
                            for i, item in enumerate(data):
                                print(f"{i + 1}. {item[0]} | Pajak: {item[1]} | Status: {item[2]}")

                    elif pilihan_admin == "2":
                        plat = input("Masukkan plat nomor: ")
                        pajak = input("Masukkan harga pajak: ")
                        status = input("Masukkan status pembayaran: ")

                        data.append([plat, (pajak), (status)])
                        print(f"Data {plat} berhasil ditambahkan")
                        
                    elif pilihan_admin == "3":
                        if len(data) == 0:
                            print("Data kosong")
                        else:
                            for i, item in enumerate(data):
                                print(f"{i + 1}. {item[0]} | Pajak: {item[1]} | Status: {item[2]}")

                            index = input("Masukkan Nomor Data Yang Ingin Diupdate: ")

                            if (index) and 0 < int(index) <= len(data):
                                index = int(index) - 1
                                plat_baru = input("Masukkan Nomor Plat Baru (Klik enter jika tidak diubah): ")
                                pajak_baru = input("Masukkan Harga Pajak baru (Klik enter jika tidak diubah): ")
                                status_baru = input("Masukkan status pembayaran (Klik enter jika tidak diubah): ")
                                os.system("cls")

                                data[index][0] = plat_baru
                                data[index][1] = (pajak_baru)
                                data[index][2] = (status_baru)
                                print("Data berhasil diupdate")
                            else:
                                print("Data Yang Dipilih tidak valid")

                    elif pilihan_admin == "4":
                        if len(data) == 0:
                            print("Data kosong")
                        else:
                            for i, item in enumerate(data):
                                print(f"{i + 1}. {item[0]} | Pajak: {item[1]} | Status: {item[2]}")

                            index = input("Masukkan nomor data yang ingin dihapus: ")

                            if(index) and 0 < int(index) <= len(data):
                                index = int(index) - 1
                                del data[index]
                                print(f"Data {item[0]} berhasil dihapus")
                            else:
                                print("Data Yang Dipilih tidak valid")

                    elif pilihan_admin == "5":
                        break

                    else:
                        print("Pilihan tidak valid")

                else:
                    os.system("cls")
                    print("---- User ----")
                    print("1. Tampilkan Data")
                    print("2. logout")
                    pilihan_user = input("Pilih menu: ")

                    if pilihan_user == "1":
                        if len(data) == 0:
                            print("Data Kosong")
                        else:
                            for i, item in enumerate(data):
                                print(f"{i + 1}. {item[0]} | Pajak: {item[1]} | Status: {item[2]}")

                    elif pilihan_user == "2":
                        break

                    else:
                        print("Pilihan tidak valid")
                    
    elif pilihan == "3":
        print("Terima kasih telah Menggunakan Aplikasi Ini")
        break

    else:
        print("Pilihan tidak valid. Silakan coba lagi")