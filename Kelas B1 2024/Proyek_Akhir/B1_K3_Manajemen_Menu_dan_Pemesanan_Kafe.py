import os
from tabulate import tabulate

def clear():
    os.system("cls")

os.system("pip install tabulate")

users = [["admin", "admin", "admin", "admin"]]

menu =  [["Americano", 18000],
        ["Espresso", 15000],
        ["Coffe Latte", 22000],
        ["Latte Macchiato", 23000],
        ["Caramel Macchiato", 25000],
        ["Cafe Frappe", 28000],
        ["Cappucino", 24000],
        ["Frozen Mocha", 27000],
        ["Smoothies", 30000],
        ["Choco Mint", 29000],
        ["Ice Cream", 18000],
        ["Apple Pie", 20000],
        ["Waffle", 22000],
        ["Cinnamon Roll", 25000],
        ["Cheese Cake", 28000]]

pesanan = {}
history = {}

def tidakbolehkosong(prompt):
    while True:
        try:
            data = input(prompt).strip()
            if not data:
                raise ValueError("Input tidak boleh kosong atau hanya spasi")
            return data
        except ValueError as e:
            print(e)

def registrasiadmin():
    while True:
        kode = tidakbolehkosong("Masukkan kode admin: ")
        if kode == kodeadmin:
            print("Kode admin benar")
            input("Klik Enter untuk melanjutkan registrasi")
            clear()
            while True:
                username = tidakbolehkosong("Buat Username: ")
                if any(user[0] == username for user in users):
                    print("Username sudah digunakan.")
                else:
                    password = tidakbolehkosong("Masukkan Password: ")
                    namalengkapadmin = tidakbolehkosong("Masukkan Nama Lengkap: ")
                    users.append([username, password, "admin", namalengkapadmin])
                    print(f"Pengguna {username} berhasil registrasi sebagai Admin.")
                    input("Klik Enter untuk melanjutkan")
                    return namalengkapadmin
                break
        else:
            print("Kode yang Anda masukkan salah.")
            continue

def registrasiuser():
    while True:
        username = tidakbolehkosong("Buat Username: ")
        if any(user[0] == username for user in users):
            print("Username sudah digunakan, silakan ganti.")
        else:
            password = tidakbolehkosong("Masukkan Password: ")
            namalengkapuser = tidakbolehkosong("Masukkan Nama Lengkap: ")
            users.append([username, password, "user", namalengkapuser])
            print(f"Pengguna {username} berhasil registrasi.")
            input("Klik Enter untuk melanjutkan")
            return namalengkapuser
        break

def lihatmenu():
    head = ["No", "Menu", "Harga"]
    tabelmenu = [[i + 1, item[0], item[1]] for i, item in enumerate(menu)]
    print(tabulate(tabelmenu, headers=head, tablefmt="fancy_outline"))

def lihatpesanan():
    print("=" * 40)
    print("            PESANAN PELANGGAN")
    print("=" * 40)
    if len(pesanan) == 0:
        print("Tidak Ada Pesanan")
        input("Klik Enter Untuk Melanjutkan")
    else:
        for index, (user_name, user_orders) in enumerate(pesanan.items(), start=1):
            total = sum(order['harga'] * order['jumlah'] for order in user_orders)
            print(f"\n {index}. Pesanan oleh {user_orders[0]['nama']}:")
            for order in user_orders:
                print(f"    {order['pesanan']} - Jumlah : {order['jumlah']}")
            print(f"    Total Harga : Rp. {total}")
            print("-" * 40)
        input("Klik Enter Untuk Melanjutkan")

def pesananselesai():
    print("=" * 40)
    print("           SELESAIKAN PESANAN")
    print("=" * 40)
    if len(pesanan) == 0:
        print("Tidak Ada Pesanan")
        input("Klik Enter Untuk Melanjutkan")
    else:
        for index, (user_name, user_orders) in enumerate(pesanan.items(), start=1):
            total = sum(order['harga'] * order['jumlah'] for order in user_orders)
            print(f"\n {index}. Pesanan oleh {user_orders[0]['nama']}:")
            for order in user_orders:
                print(f"    {order['pesanan']} - Jumlah : {order['jumlah']}")
            print(f"    Total Harga : Rp. {total}")
            print("-" * 40)

        while True:
            try:
                selesai = tidakbolehkosong("Pilih Pesanan untuk diselesaikan (0 untuk kembali): ")
                if selesai.isdigit() and 0 < int(selesai) <= len(pesanan):
                    selesai = int(selesai) - 1
                    user_name = list(pesanan.keys())[selesai]
                    user_orders = pesanan[user_name]
            
                    # Tambahkan pesanan ke history
                    if user_name not in history:
                        history[user_name] = []
                    history[user_name].extend(user_orders)
            
                    # Hapus pesanan dari dictionary pesanan
                    del pesanan[user_name]
                    print("Pesanan berhasil diselesaikan dan ditambahkan ke riwayat.")
                    input("Klik Enter Untuk Melanjutkan")
                    break
                elif selesai == "0":
                    input("Klik Enter Untuk Melanjutkan")
                    break
                else:
                    print("Nomor pesanan tidak valid")      
            except ValueError:
                print("Input Salah")

def tambahmenu():
    print("=" * 40)
    print("            TAMBAH MENU BARU")
    print("=" * 40)
    namamenu = tidakbolehkosong("Masukkan nama menu: ")
    if not namamenu:
        print("Nama Menu Tidak Boleh Kosong")
    else:
        while True:
            try:
                harga = int(tidakbolehkosong("Masukkan harga: "))
                if harga <= 0:
                    print("Harga harus lebih dari 0.")
                    continue
                menu.append([namamenu, harga])
                print(f"Menu {namamenu} berhasil ditambahkan.")
                input("Klik Enter Untuk Melanjutkan...")
                break
            except ValueError:
                print("Harga harus berupa angka.")

def updatemenu():
    while True:
        index = tidakbolehkosong("Masukkan nomor menu yang ingin diupdate (0 Untuk Kembali): ")
        if index == "0":
            break
        elif index.isdigit() and 0 < int(index) <= len(menu):
            index = int(index) - 1
            nama_baru = input("Masukkan nama menu: ")
            while True:
                try:
                    harga_baru = int(input("Masukkan harga: "))
                    if harga_baru <= 0:
                        print("Harga harus lebih dari 0.")
                        continue
                    if nama_baru:
                        menu[index][0] = nama_baru
                    if (harga_baru):
                        menu[index][1] = int(harga_baru)
                    print("Menu berhasil diupdate")
                    input("Klik Enter Untuk Melanjutkan")
                    clear()
                    return
                except ValueError:
                    print("Input Harga Harus Berupa Angka")
        else:
            print("Nomor menu tidak valid")

def hapusmenu():
    while True:
        try:
            index = tidakbolehkosong("Masukkan nomor data yang ingin dihapus (0 Untuk Kembali): ")
            if index.isdigit() and 0 < int(index) <= len(menu):
                index = int(index) - 1
                datahapus = menu[index][0]
                del menu[index]
                print(f"Menu {datahapus} berhasil dihapus")
                input("Klik Enter Untuk Melanjutkan")
                break
            elif index == "0":
                input("Klik Enter Untuk Melanjutkan")
                break
            else:
                print("Menu Yang Dipilih tidak Ada")
        except ValueError:
            print("Input Tidak Valid")

def historyadmin():
    print("=" * 50)
    print("             RIWAYAT PESANAN PELANGGAN")
    print("=" * 50)
    if len(history) == 0:
        print("Belum ada pesanan dari pengguna.")
        input("Klik Enter Untuk Melanjutkan")
    else:
        for user_name, user_orders in history.items():
            if user_orders:  # Pastikan ada pesanan untuk ditampilkan
                print(f"\nPesanan oleh {user_orders[0]['nama']} (Username: {user_name}):")
                total = 0  # Inisialisasi total harga untuk user ini

                for i, order in enumerate(user_orders):
                    print(f"{i + 1}. {order['pesanan']} - Jumlah: {order['jumlah']} - Harga per pcs: {order['harga']}")
                    total += order['harga'] * order['jumlah']  # Hitung total harga untuk pesanan ini

                # Tampilkan total harga sekali setelah semua pesanan ditampilkan
                print(f"    Total Harga: Rp. {total}")
                print("-" * 50)
        input("Klik Enter Untuk Melanjutkan")

def buatpesanan():
    username = user[0]
    if username not in pesanan:
        pesanan[username] = []

    while True:
        order_number = tidakbolehkosong("Masukkan nomor menu yang ingin dipesan (0 Untuk Kembali): ")
        if order_number == "0":
            input("Klik Enter Untuk Melanjutkan")
            break

        if order_number.isdigit():
            order_number = int(order_number) - 1
            if 0 <= order_number < len(menu):
                while True:
                    try:
                        jumlah = int(tidakbolehkosong("Jumlah: "))
                        if jumlah <= 0:  # Jumlah tidak boleh kurang dari atau sama dengan nol
                            print("Jumlah harus lebih dari 0")
                            continue
                        pesanan[username].append({
                            "nama": user[3],
                            "pesanan": menu[order_number][0],
                            "harga": menu[order_number][1],
                            "jumlah": jumlah
                        })
                        total = sum(order['harga'] * order['jumlah'] for order in pesanan[username])
                        print(f"Pesanan {menu[order_number][0]} berhasil ditambahkan")
                        print(f"Total harga pesanan Anda adalah : Rp. {total}")
                        input("Klik Enter Untuk Melanjutkan")
                        return
                    except ValueError:
                        print("Jumlah Harus Berupa Angka")
            else:
                print("Menu yang dipilih tidak ada")
        else:
            print("Input tidak valid. Harus berupa angka")

def lihatpesananuser():
    print("=" * 40)
    print("           LIHAT PESANAN SAYA")
    print("=" * 40)
    username = user[0]
    if username in pesanan:
        print("Pesanan Anda :")
        total = 0
        for i, order in enumerate(pesanan[username]):
            print(f"{i + 1}. {order['pesanan']} - Jumlah: {order['jumlah']}")
            total += order['harga'] * order['jumlah']
        print(f"Total Harga Pesanan Anda : Rp. {total}")
        print("-" * 40)
        input("Klik Enter Untuk Melanjutkan")
    else:
        print("Belum ada pesanan.")
        input("Klik Enter Untuk Melanjutkan")

def ubahpesanan():
    print("=" * 40)
    print("          UBAH PESANAN")
    print("=" * 40)
    username = user[0]
    if username in pesanan:
        print("Pesanan Anda :")
        total = 0
        for i, order in enumerate(pesanan[username]):
            print(f"{i + 1}. {order['pesanan']} - Jumlah: {order['jumlah']}")
            total += order['harga'] * order['jumlah']
        print(f"Total Harga Pesanan Anda : Rp. {total}")
        print("-" * 40)
                            
        while True:
            index = tidakbolehkosong("Masukkan Nomor Menu Yang Ingin Diganti (0 Untuk Kembali): ")

            if index == "0":
                break

            elif index.isdigit() and 0 < int(index) <= len(pesanan[username]):
                index = int(index) - 1
                print("[1]. Ubah Jumlah Pesanan\n[2]. Hapus Pesanan")
                pilihanubah = tidakbolehkosong("Masukkan Pilihan: ")
                if pilihanubah == "1":
                    while True:
                        try:
                            jumlahbaru = int(tidakbolehkosong("Masukkan jumlah baru: "))
                            if jumlahbaru <= 0:
                                print("Harga harus lebih dari 0.")
                                continue
                            pesanan[username][index]['jumlah'] = jumlahbaru
                            print(f"Jumlah pesanan {pesanan[username][index]['pesanan']} telah diubah menjadi {jumlahbaru}")
                            input("Klik Enter Untuk Melanjutkan...")
                            return
                        except ValueError:
                            print("Jumlah Harus Berupa Angka")
                                    
                elif pilihanubah == "2":
                    orderhapus = pesanan[username].pop(index)
                    print(f"Pesanan {orderhapus['pesanan']} telah dihapus.")
                else:
                    print("Pilihan Salah")

            else:
                print("Nomor pesanan tidak valid.")

    else:
        print("Belum ada pesanan.")
        input("Klik Enter Untuk Melanjutkan...")

def historyuser():
    print("=" * 40)
    print("          RIWAYAT PESANAN SAYA")
    print("=" * 40)
    if username in history:
        print("History Anda :")
        total = 0
        for i, order in enumerate(history[username]):
            print(f"{i + 1}. {order['pesanan']} - Jumlah: {order['jumlah']}")
            total += order['harga'] * order['jumlah']
        print(f"Total Harga Pesanan Anda : Rp. {total}")
        print("-"*40)
        input("Klik Enter Untuk Melanjutkan")
    else:
        print("Belum ada pesanan.")
        input("Klik Enter Untuk Melanjutkan")


kodeadmin = "admin1234"

while True:
    clear()
    print("=" * 40)
    print("           KAFE RUANG RASA  ")
    print("    Silahkan login terlebih dahulu")
    print("    Register jika belum punya akun")
    print("=" * 40)
    print(" [1]. Register")
    print(" [2]. Login")
    print(" [3]. Keluar")
    print("-" * 40)
    pilihan = tidakbolehkosong("Pilih menu: ")
    input("Klik enter untuk melanjutkan")
    clear()

    if pilihan == "1":
        print("=" * 40)
        print("              PILIH ROLE")
        print("=" * 40)
        print("[1]. Registrasi sebagai admin \n[2]. Registrasi sebagai pengunjung")
        print("-"*40)
        registrasi = tidakbolehkosong("Masukkan Pilihan : ")
        input("Klik enter untuk melanjutkan")
        clear()

        if registrasi == "1":
            registrasiadmin()
            clear()

        elif registrasi == "2": 
            registrasiuser()
            clear()

        else:
            print("Pilihan Tidak Valid")

    elif pilihan == "2":
        print("=" * 40)
        print("             SILAHKAN LOGIN")
        print("=" * 40)
        username = tidakbolehkosong("Username: ")
        password = tidakbolehkosong("Password: ")
        user = None

        for i in users:
            if i[0] == username and i[1] == password:
                user = i
                break

        if user is None:
            print("Login Gagal, Username atau Password Salah")
            input("Klik enter untuk kembali ke menu utama")
            
        else:
            print("Selamat anda berhasil login")
            input("Klik enter untuk masuk ke menu")
            clear()

            if user[2] == "admin":
                # Menu admin
                while True:
                    print("="*30)
                    print("          MENU ADMIN ")
                    print("="*30)
                    print("[1]. Lihat Menu\n[2]. Lihat Pesanan\n[3]. Selesaikan Pesanan\n[4]. Tambah Menu\n[5]. Update Menu\n[6]. Hapus Menu\n[7]. Riwayat Pembelian\n[8]. Logout")
                    print("-"*30)
                    pilihanadmin = tidakbolehkosong("Masukkan Pilihan : ")
                    input("Klik enter untuk melanjutkan")
                    clear()

                    if pilihanadmin == "1":
                        print("="*38)
                        print("        MENU KAFE RUANG RASA")
                        print("="*38)
                        lihatmenu()
                        input("Klik Enter Untuk Melanjutkan")
                        clear()

                    elif pilihanadmin == "2":
                        lihatpesanan()
                        clear()

                    elif pilihanadmin == "3":
                        pesananselesai()
                        clear()

                    elif pilihanadmin == "4":
                        tambahmenu()
                        clear()

                    elif pilihanadmin == "5":
                        print("=" * 38)
                        print("            PERBARUI MENU")
                        print("=" * 38)
                        lihatmenu()
                        updatemenu()
                        clear()

                    elif pilihanadmin == "6":
                        print("=" * 38)
                        print("            HAPUS MENU")
                        print("=" * 38)
                        lihatmenu()
                        hapusmenu()
                        clear()

                    elif pilihanadmin == "7":
                        historyadmin()
                        clear()

                    elif pilihanadmin == "8":
                        break
                    else:
                        print("Pilihan tidak valid.")
                        input("Klik enter untuk memilih menu lagi")

            elif user[2] == "user":
                # Menu user
                while True:
                    print("="*30)
                    print("        MENU PENGUNJUNG ")
                    print("="*30)
                    print("[1]. Lihat Menu\n[2]. Tambah Pesanan\n[3]. Lihat Pesanan\n[4]. Ubah Pesanan\n[5]. Riwayat Pembelian\n[6]. Logout")
                    print("-"*30)
                    pilihanuser = tidakbolehkosong("Masukkan Pilihan : ")
                    input("Klik enter untuk melanjutkan")
                    clear()

                    if pilihanuser == "1":
                        print("="*38)
                        print("        MENU KAFE RUANG RASA")
                        print("="*38)
                        lihatmenu()
                        input("Klik Enter Untuk Melanjutkan")
                        clear()

                    elif pilihanuser == "2":
                        print("=" *38)
                        print("          BUAT PESANAN BARU")
                        print("=" *38)
                        lihatmenu()
                        buatpesanan()
                        clear()

                    elif pilihanuser == "3":
                        lihatpesananuser()
                        clear()

                    elif pilihanuser == "4":
                        ubahpesanan()
                        clear()

                    elif pilihanuser == "5":
                        historyuser()
                        clear()

                    elif pilihanuser == "6":
                        break
                    else:
                        print("Pilihan tidak valid.")
                        input("Klik enter untuk memilih menu lagi")

    elif pilihan == "3":
        print("Terimakasih telah menggunakan aplikasi ini")
        break

    else:
        clear()
        print("Input tidak valid.")
        input("Klik enter untuk memilih menu lagi")