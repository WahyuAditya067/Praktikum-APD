import os

data = [
    {
        "Plat" : "KT 1000 AA",
        "Pajak" : 100000,
        "status" : "Lunas"
    }
]

def clear():
    os.system("cls")

totaldata = len(data)

def menuadmin():
    print("--- Menu Admin ---")
    print("1. Tampilkan Data")
    print("2. Tambah Data")
    print("3. Update Data")
    print("4. Hapus Data")
    print("5. Logout")
    
def dataawal():
    global totaldata
    if len(data) == 0:
        print("Data kosong")
    else:
        for i, item in enumerate(data):
            print(f"{i + 1}. {item['Plat']} | Pajak: {item['Pajak']} | Status: {item['status']}")
        print(f"Total kendaraan yang terdaftar adalah {totaldata}")

def datatambah():
    global totaldata
    plat = input("Masukkan plat nomor: ")
    pajak = input("Masukkan harga pajak: ")
    status = input("Masukkan status pembayaran: ")

    data.append({
        "Plat" : plat,
        "Pajak" : pajak,
        "status" : status
    })
    totaldata += 1
    return plat
    

def dataupdate(plat_baru, pajak_baru, status_baru):
    index = input("Masukkan Nomor Data Yang Ingin Diupdate: ")

    if (index) and 0 < int(index) <= len(data):
        index = int(index) - 1
        plat_baru = input("Masukkan Nomor Plat Baru (Klik enter jika tidak diubah): ")
        pajak_baru = input("Masukkan Harga Pajak baru (Klik enter jika tidak diubah): ")
        status_baru = input("Masukkan status pembayaran (Klik enter jika tidak diubah): ")
        clear()

        data[index]["Plat"] = plat_baru
        data[index]["Pajak"] = pajak_baru
        data[index]["status"] = status_baru
        print("Data berhasil diupdate")
    else:
        print("Data Yang Dipilih tidak valid")

def hapusdata():
    global totaldata
    index = input("Masukkan nomor data yang ingin dihapus: ")

    if(index) and 0 < int(index) <= len(data):
        index = int(index) - 1
        datahapus = data[index]["Plat"]
        del data[index]
        totaldata -= 1
        return datahapus
    else:
        print("Data Yang Dipilih tidak valid")