# #variable akan bernukau false jika string kosong, 0, [], (), {}, false
# uang = 1
# if uang:
#     print("Pergi ke pasar")
# else:
#     print("pergi entah kemana")


# nilai = 70
# if nilai < 70:
#     print("Tidak lulus")
# else:
#     print("Lulus")


# nilai = 1
# if nilai > 0:
#     print("positif")
# else:
#     print("negatif")

# umur = int(input("Masukkan umur anda :"))

# if umur <= 10:
#     print("Anak-anak)")
# elif umur <= 18:
#     print("remaja")
# elif umur <= 35:
#     print("dewasa")
# elif umur <= 60:
#     print("Tua")
# else:
#     print("paruh baya")

# nilai1 = 76

# if nilai1 >= 80 :
#     if nilai1 >= 85 :
#         print("Nilai A+")
#     else :
#         print("Nilai A-")
# else:
#     print("Tidak lulus")

print("menu")
print("1. nonton film")
print("2. Ngoding")
print("3.")

kegiatan = int(input("kegiatan anda : "))
if kegiatan == 1:
    print("Sedang Nonton film")
elif kegiatan == 2:
    print("Sedang ngoding")
elif kegiatan == 3:
    print("keluar dari aplikasi")
else:
    print("kegiatan tidak tersedia")

angka = 10

#kalo if dan if, yg kondisi bawah juga dicek apapun hasil yg atas
if angka % 2 ==0:
    print("Genap")
if angka > 0:
    print("Positif")

#kalo if dan elif, jika kondisi yg atas benar, yg bawah ga dicek
if angka % 2 ==0:
    print("Genap")
elif angka > 0:
    print("Positif")


