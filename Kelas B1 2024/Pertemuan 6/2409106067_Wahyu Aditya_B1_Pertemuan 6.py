data_mhs = {
    "nama" : "ucup",
    "nim" : 1,
    "matkul" : ["APD", "Kalkulus", "Jarkom"],
    "dosen" : {
        "nama" : "Pak Awang",
        "matkul" : "APD"
    }
}

#print(data_mhs["dosen"]["nama"])

#for value in data_mhs.keys():
    #print(value)

    #print(data_mhs[keys])
    #sama aja kayak diatas

data_mhs2 = [
    {
    "nama" : "ucup",
    "role" : "admin"
    },

    {
    "nama" : "michael",
    "role" : "user"
    },
]

print(data_mhs2[0]["nama"])
print(data_mhs2[1]['nama'])

#cache = data_mhs.pop("nim")

#data_mhs["id"] = cache

#print(data_mhs)
#print(cache)

#print("Jumlah Data = ", len(data_mhs))


#key = "apel", "jeruk", "mangga", "semangka", "anggur"
#value = 1
#buah = dict.fromkeys(key, value)
#print(buah)


#data_mhs["alamat"] = "Samarinda"

#data_mhs.update({"alamat": "Tenggarong"})

#print(data_mhs)

#print(data_mhs.get("Mapel", "Data ga ada"))
#pake get buat error handling

#for data in data_mhs:
    #print(data)

#for key_data, value_data in data_mhs:
    #print(f"Key : {key_data}\n Value: {value_data}")

#print(data_mhs["nama"])
#print(data_mhs["nim"])
#print(data_mhs)

#Nilai = {
    #"Matematika" : 80,
    #"B. Indonesia" : 90,
    #"B. Inggris" : 81,
    #"kimia" : 20
#}

#sebelum Setdefault
#print(Nilai)
#print("")

#menggunakan setdefault
#print("Nilai : ", Nilai.setdefault("Kimia", 70))
#print("")

#setelah menggunakan setdefault
#print(Nilai)