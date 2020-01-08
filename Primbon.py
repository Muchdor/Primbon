import random

a = 100
b = 200

print("==֍==SELAMAT DATANG DI ABAL-ABAL METER==֍==")
c = input("1. Lanjut \n2. Keluar \n")
if c == '1':
    print("Mantap")

    print("=================")

    loop = True
    while loop:

        cowok = input("Masukkan nama cowok : ")
        while a <= 0 or a >= 32:
            a = int(input("Masukkan tanggal lahir (1-31) : "))

        cewek = input("Masukkan nama cewek : ")
        while b <= 0 or b >= 32:
            b = int(input("Masukkan tanggal lahir (1-31) : "))

        hasil = a + b
        print("====================")

        print("Nama cowok adalah :" + cowok)
        print("Tangal lahir cowok : ", a)

        print("Nama cewek adalah :" + cewek)
        print("Tanggal lahir cewek : ", b)

        print("===================")

        confirm = input("Apakah nama yang anda masukkan sudah benar? y/n: ")

        if confirm == 'y':
            loop = False

    if hasil > 45:
        match = random.randrange(75, 100)
    elif hasil > 30:
        match = random.randrange(50, 74)
    elif hasil > 15:
        match = random.randrange(25, 49)
    else:
        match = random.randrange(0, 24)

    print('Abal-abal Meter anda adalah', match, '%')

    if match >= 80:
        print("Selamat anda pasangan yang serasi")
    elif match >= 60:
        print("Masih bisa dirundingkan lagi")
    elif match >= 40:
        print("Yakin...??")
    elif match >= 20:
        print("Cari lagi")
    else:
        print("Maaf, menurut kita anda tidak cocok")
else:
    print("==֍==Selamat berkunjung kembali==֍==")