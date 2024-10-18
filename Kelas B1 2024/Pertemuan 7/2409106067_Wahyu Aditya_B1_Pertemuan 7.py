import os

#def hasil(nama):
    #print("Hello world " + nama)

#hasil("Tes")
#hasil("Tes2")
#hasil("Tes3")

def luas_persegipanjang(panjang, lebar):
    luas = panjang * lebar
    #print(f"Luas persegi panjang dengan panjang {panjang} dan lebar {lebar} adalah {luas}")
    return luas
#luas_persegipanjang(10, 5)
luas_persegi = luas_persegipanjang(10, 5)
print(luas_persegi)

nama = "Dimas" #variabel global

def say_hello():
    nama = "Daffa" #variabel lokal
    print(nama, "dalam fungsi")

print(nama, "luar fungsi")
say_hello()

def faktorial (n):
    if n == 1:
        return 1
    else:
        return n * faktorial(n-1)
print(faktorial(5))

def sayhello():
    nama = "Dimas"
    print("Hello")
    print("world")
    return nama

sayhello()

def sayhello2():
    while True:
        pilihan = input("1 untuk berhenti 2 untuk lanjut")
        if pilihan == "1":
            return
            print("")
        os.system("cls")

sayhello2()