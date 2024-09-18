nama = str(input("Masukkan Nama : "))
umur = int(input("Masukkan Umur : "))
tb = float(input("Masukkan tinggi badan : "))
bb = float(input("Masukkan berat badan : "))
status_input = int(input("Jenis kelamin anda (0 jika Laki-laki, 1 = Wanita) : "))
status = bool(status_input)

width = 90

print("=" * width)
print("Biodata Anda".center(width))
print("=" * width)

if status == False :
    jenis_kelamin = ("Laki-laki")
else :
    jenis_kelamin = ("Wanita")

print(f"Nama           : {nama}")
print(f"Umur           : {umur} tahun")
print(f"Tinggi Badan   : {tb} cm")
print(f"Berat Badan    : {bb} kg")
print(f"Jenis Kelamin  : {jenis_kelamin}")
print(f"umur + tb + bb :{umur + tb + bb}")

print("=" * width)
